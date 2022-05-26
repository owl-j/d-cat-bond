API_SLASH = "/"


def wrapping_refreshing(func):
    def wrapped(self):
        got = func(self)
        self.refresh_base()
        return got

    return wrapped


class ApiPatternConstructor:
    def __init__(self):
        self.base = ""
        self.api_slash = API_SLASH

    def refresh_base(self):
        self.base = ""

    def _combine_one(self, component):
        self.base = self.api_slash.join([self.base, component])

    def combine(self, *paths):
        for path in paths:
            self._combine_one(path)
        got = self.base
        self.refresh_base()
        return got


class CatBondSvcApiConstructor(ApiPatternConstructor):
    def __init__(self):
        super().__init__()
        self.base = ""

    @property
    @wrapping_refreshing
    def tiles_validation_GET(self):
        return self.combine("tiles-validation")

    @property
    @wrapping_refreshing
    def tiles_sensors_observation_GET(self):
        return self.combine("tiles-sensors-observation")
