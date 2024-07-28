# module to maintain database related utility constants and functions

import sqlobject
import time
from typing import Callable, Iterable, Mapping

from falcon1.Interface.DB.Base import *


def exponential_backoff(
        fn: Callable, args: Union[Iterable, None] = None, kwargs: Union[Mapping, None] = None,
        retries: int = 3, incremental_rate: int = 2
):
    """
    Helper function for DB connections using exponential backoff.
    :param fn: Function to execute.
    :param args: Arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :param retries: Number of times to retry.
    :param incremental_rate: Rate at which to increment the exponential backoff.
    """
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    sleep_time = 1
    error = None
    while retries > 0:
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            retries -= 1
            error = e
            time.sleep(sleep_time)
            sleep_time *= incremental_rate
    raise error


CLICKHOUSE_TABLES = {
    "TRANSACTIONS": (
        """
        transactions (
            request_id UUID,
            external_request_id UUID,
            http_method Enum8('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'),
            path String,
            start_time DateTime,
            end_time DateTime,
            http_status String
        )
        """,
        "StripeLog"
    )
}


def make_db_connection(db_type: DBType):
    # Establish Database Connection

    if db_type == DBType.MYSQL:
        # MySQL Connection
        mysql_api = DBAPI(
            db_type=DBType.MYSQL, host="mysql", port=3306,
            user="roci", password="roci-root", db="falcon1"
        )
        mysql_conn = exponential_backoff(mysql_api.connect)
        return mysql_conn

    elif db_type == DBType.CLICKHOUSE:
        # ClickHouse Connection
        clickhouse_api = DBAPI(
            db_type=DBType.CLICKHOUSE, host="clickhouse", port=8443,
            user="default", password="roci", db="default"
        )
        clickhouse_conn = exponential_backoff(clickhouse_api.connect)
        clickhouse_api.create_tables(CLICKHOUSE_TABLES["TRANSACTIONS"])  # create clickhouse tables
        return clickhouse_conn


GLOBAL_DB_CONNECTIONS = {
    DBType.MYSQL: None,
    DBType.CLICKHOUSE: None,
}


def init_db() -> None:
    # initialize MySQL DB
    mysql_conn = make_db_connection(DBType.MYSQL)

    # initialize ClickHouse DB
    _ = make_db_connection(DBType.CLICKHOUSE)

    sqlobject.sqlhub.processConnection = mysql_conn  # default connection
