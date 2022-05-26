class Builder:
    def build(self):
        pass


class SqlQueryBuilder(Builder):
    def __init__(self):
        self.deliminator = " "

    def query_build(self, iterable):
        return self.deliminator.join(iterable)
