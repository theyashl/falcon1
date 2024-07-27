# Establish Database Connection
import time
from typing import Callable, Iterable, Mapping, Union

from falcon1.Interface.DB.Base import *
from falcon1.Interface.DB.ClickHouse import TABLES


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


# MySQL Connection
mysql_api = DBAPI(
    db_type=DBType.MYSQL, host="127.0.0.1", port=3306,
    user="roci", password="roci-root", db="falcon1"
)
mysql_conn = exponential_backoff(mysql_api.connect)

# ClickHouse Connection
clickhouse_api = DBAPI(
    db_type=DBType.CLICKHOUSE, host="localhost", port=8443,
    user="default", password="roci", db="default"
)
clickhouse_conn = exponential_backoff(clickhouse_api.connect)

clickhouse_api.create_tables(TABLES["TRANSACTIONS"])  # create clickhouse tables

conn = mysql_conn  # default connection
