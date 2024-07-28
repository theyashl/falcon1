# module to manage the config variables
import os
from typing import Any

# constants
mysql_configs = None
clickhouse_configs = None


# util classes

class BaseConfig(dict):
    CONFIG_DICT: dict[str, tuple[type, Any]] = {}

    def load(self):
        """
        load config variables in memory from environment
        """
        for key, value in self.CONFIG_DICT.items():
            value_type = value[0]
            default_value = value[1]
            self[key] = value_type(os.environ.get(key, default_value))

    def __getattr__(self, attr):
        if attr not in self.CONFIG_DICT:
            raise ValueError(f"Attribute '{attr}' not defined")
        return self[attr]

    def __setattr__(self, attr, value):
        raise ValueError("Setting attributes is not allowed")


class MySQLConfig(BaseConfig):
    """
    Holds config variables for MySQL DB
    """
    CONFIG_DICT = {  # variable name: (type, default value)
        "MYSQL_DATABASE": (str, "falcon1"),
        "MYSQL_USER": (str, "falcon_user"),
        "MYSQL_PASSWORD": (str, "falcon_user"),
        "MYSQL_HOST": (str, "127.0.0.1"),
        "MYSQL_PORT": (int, 3306)
    }


class CLICKHOUSEConfig(BaseConfig):
    """
    Holds config variables for ClickHouse DB
    """
    CONFIG_DICT = {  # variable name: default value
        "CLICKHOUSE_HOST": (str, "localhost"),
        "CLICKHOUSE_PORT": (int, 8443),
        "CLICKHOUSE_DB": (str, "default"),
        "CLICKHOUSE_USER": (str, "default"),
        "CLICKHOUSE_PASSWORD": (str, "default"),
    }


# util functions

def init_configs():
    """
    Initialize config variables, will be accessible using global variables
    """
    global mysql_configs, clickhouse_configs

    # mysql configs
    mysql_configs = MySQLConfig()
    mysql_configs.load()

    # clickhouse configs
    clickhouse_configs = CLICKHOUSEConfig()
    clickhouse_configs.load()
