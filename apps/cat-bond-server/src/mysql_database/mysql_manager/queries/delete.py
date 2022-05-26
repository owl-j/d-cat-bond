from mysql_database.mysql_manager.queries import wrap
from mysql_database.mysql_manager.queries.where import where

_template = "DELETE FROM {table} {where_constraints};"


def delete(table_name, constraints):
    if constraints is None:
        constraints = []
    if type(constraints) is dict:
        constraints = [
            "{column} = {value}".format(column=k, value=wrap(v))
            for k, v in constraints.items()
        ]
    return _template.format(table=table_name, where_constraints=where(constraints))
