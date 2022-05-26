from mysql_database.mysql_manager import my_connection_pool
from mysql_database.mysql_manager.core.manager import MySQLManager
from utils.cat_bond_server_config_manager import CatBondServerConfigureManager

config = CatBondServerConfigureManager()
mysql_manager = MySQLManager(connection_pool=my_connection_pool)


def handle_api_tiles_validation_GET(got):
    raise NotImplementedError


def handle_api_tiles_sensors_observation_GET(got):
    raise NotImplementedError
