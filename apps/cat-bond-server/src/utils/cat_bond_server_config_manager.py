from configparser import ConfigParser

from utils.repo_path_manager import RepoPathManager


class CatBondServerConfigureManager:
    def __init__(self):
        config = ConfigParser()
        repo_path = RepoPathManager()
        # config is initialised from the central_config
        config.read(repo_path.cat_bond_server_config)
        self.config = config
        self.registered_config_managers = []

    def __add__(self, other_configure_manager):
        self.register_config_manager(other_configure_manager)

    def register_config_manager(self, other_configure_manager):
        self.registered_config_managers.append(other_configure_manager)

    def get_val(self, section, key):
        return self.config.get(section, key)

    def get_int_val(self, section, key):
        return getattr(self.config, "getint")(section, key)

    def get_float_val(self, section, key):
        return getattr(self.config, "getfloat")(section, key)

    def get_bool_val(self, section, key):
        return getattr(self.config, "getboolean")(section, key)
