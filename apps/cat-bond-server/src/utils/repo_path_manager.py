import os


def _wrapping_refreshing(func):
    def wrapped(self):
        got = func(self)
        self.refresh_base()
        return got

    return wrapped


class RepoPathManager:
    def __init__(self):
        self.base = ""

    def refresh_base(self):
        self.base = ""

    def _combine_one(self, component):
        self.base = os.path.join(self.base, component)

    def combine(self, *directed_folders):
        for folder in directed_folders:
            self._combine_one(folder)
        got = self.base
        self.refresh_base()
        return got

    def find_root(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("cat-bond-server") + 1])
        return self

    def find_src(self):
        explore = str(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        self.base = os.path.sep.join(explore[: explore.index("src") + 1])
        return self

    @property
    @_wrapping_refreshing
    def dot_env_dev(self):
        self.find_root()
        return self.combine(".env.dev")

    @property
    @_wrapping_refreshing
    def dot_env_prod(self):
        self.find_root()
        return self.combine(".env.prod")

    @property
    @_wrapping_refreshing
    def cat_bond_server_config(self):
        self.find_src()
        return self.combine("central_config", "cat_bond_server.ini")
