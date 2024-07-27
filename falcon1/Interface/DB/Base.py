"""
Database Connectionn Interface
"""
from abc import ABC, abstractmethod
from enum import IntEnum


class DBType(IntEnum):
    MYSQL = 1
    CLICKHOUSE = 2

class DBAPI(ABC):
    _registry = {}

    @classmethod
    def _verify_db_type(cls, db_type):
        try:
            db_type in DBType
        except TypeError:
            raise TypeError("DBType Enum is expected in db_type")

    def __init_subclass__(cls, db_type, **kwargs):
        super().__init_subclass__()
        cls._verify_db_type(db_type)
        cls._registry[db_type] = cls

    def __new__(cls, *args, **kwargs):
        if args:
            db_type = args[0]
        else:
            db_type = kwargs.get("db_type")
        if not db_type:
            raise TypeError("missing or invalid required 'db_type' argument")
        cls._verify_db_type(db_type)
        subclass = cls._registry[db_type]
        return super().__new__(subclass)
    
    def __init__(self, db_type, host, port, user, password, db, **kwargs) -> None:
        self.db_type = db_type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.kwargs = kwargs

    @abstractmethod
    def connect(self):
        raise NotImplementedError
    
    @abstractmethod
    def create_tables(self):
        pass
