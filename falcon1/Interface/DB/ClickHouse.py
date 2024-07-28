"""
ClickHouse engine implementation
"""
from falcon1.Interface.DB.Base import DBAPI, DBType
import clickhouse_connect


class ClickHouseAPI(DBAPI, db_type=DBType.CLICKHOUSE):
    _CLIENT = None
    
    def __init__(self, db_type, host, port, user, password, db) -> None:
        super().__init__(db_type, host, port, user, password, db)

    def connect(self):
        if not self._CLIENT:
            self._CLIENT = clickhouse_connect.get_client(host=self.host, username=self.user, password=self.password)
            self._set_global_connection(self._CLIENT)
        return self._CLIENT

    def create_tables(self, *args, **kwargs):
        for table in args:
            table_def, engine = table
            self._CLIENT.command(f'CREATE TABLE IF NOT EXISTS {table_def} ENGINE {engine}')
