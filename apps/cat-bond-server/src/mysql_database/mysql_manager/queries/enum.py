from mysql_database.mysql_manager.helpers.checkers import \
    iterable_and_not_string
from mysql_database.mysql_manager.queries import wrap

_template = "ENUM ({content})"


def enum(items):
    assert iterable_and_not_string(items), "items should be iterable."
    return _template.format(content=", ".join([wrap(item) for item in items]))
