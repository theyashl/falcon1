# Establish Database Connection
from falcon1.Interface.DB.Base import *
from falcon1.Interface.DB.ClickHouse import TABLES


# MySQL Connection
mysql_api = DBAPI(
    db_type=DBType.MYSQL, host="localhost", port=3306,
    user="roci", password="root-roci", db="falcon1"
)
mysql_conn = mysql_api.connect()


# ClickHouse Connection
clickhouse_api = DBAPI(
    db_type=DBType.CLICKHOUSE, host="localhost", port=8443,
    user="default", password="roci", db="default"
)
clickhouse_conn = clickhouse_api.connect()

clickhouse_api.create_tables(TABLES["TRANSACTIONS"]) # create clickhouse tables


conn = mysql_conn # default connection
