"""
MySQL engine implementation
"""
from falcon1.Interface.DB.Base import DBAPI, DBType
from sqlobject.mysql import builder

class MySQLAPI(DBAPI, db_type=DBType.MYSQL):
    def __init__(self, db_type, host, port, user, password, db, **kwargs) -> None:
        super().__init__(db_type, host, port, user, password, db, **kwargs)

    def connect(self):
        conn = builder()(
            user=self.user, password=self.password, host=self.host, db=self.db, **self.kwargs
        )
        return conn
    
    def create_tables(self):
        return super().create_tables()
