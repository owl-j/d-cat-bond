import uuid

from loguru import logger
from mysql.connector import pooling

from utils.cat_bond_server_config_manager import CatBondServerConfigureManager

cat_bond_server_config_manager = CatBondServerConfigureManager()


class ConnectionPool:
    def __init__(self):
        # 32 is the maximum pool size.
        self.cnx_pool = pooling.MySQLConnectionPool(
            pool_name="peep_pool_{id}".format(id=uuid.uuid4()),
            pool_size=cat_bond_server_config_manager.get_int_val(
                "mysql_manager", "pool_size"
            ),
            host=cat_bond_server_config_manager.get_val("mysql_manager", "host"),
            port=cat_bond_server_config_manager.get_val("mysql_manager", "port"),
            database=cat_bond_server_config_manager.get_val(
                "mysql_manager", "database"
            ),
            user=cat_bond_server_config_manager.get_val("mysql_manager", "user"),
            password=cat_bond_server_config_manager.get_val(
                "mysql_manager", "password"
            ),
        )
        logger.debug("MySQL Database has been successfully connected!")

    def get_connection(self):
        return self.cnx_pool.get_connection()
