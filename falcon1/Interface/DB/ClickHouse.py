"""
ClickHouse engine implementation
"""
from enum import Enum
from falcon1.Interface.DB.Base import DBAPI, DBType
import clickhouse_connect

TABLES = {
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

class ClickHouseAPI(DBAPI, db_type=DBType.CLICKHOUSE):
    _CLIENT = None
    
    def __init__(self, db_type, host, port, user, password, db) -> None:
        super().__init__(db_type, host, port, user, password, db)

    def connect(self):
        if not self._CLIENT:
            self._CLIENT = clickhouse_connect.get_client(host=self.host, username=self.user, password=self.password)
        return self._CLIENT
    
    def create_tables(self, *args):
        for table in args:
            table_def, engine = table
            self._CLIENT.command(f'CREATE TABLE IF NOT EXISTS {table_def} ENGINE {engine}')
