from mysql_database.mysql_manager.helpers.checkers import iterable
from mysql_database.mysql_manager.queries import wrap

_template = "WHERE {constraints}"


def _logical_join(constraints):
    if isinstance(constraints, str):
        return constraints

    if isinstance(constraints, list):
        return " AND ".join(
            ["({})".format(_logical_join(constraint)) for constraint in constraints]
        )
    return " OR ".join(
        ["({})".format(_logical_join(constraint)) for constraint in constraints]
    )


def where(constraints):
    """
    constraints is an iterable of strings(constraints), for example:

    ["A > B", "B > C", "C > D or D > E"] (case 1)
    or
    ("A > B", "B > C", "C > D and D > E") (case 2)
    or
    {"A": "B", "C":"D"} (case 3)

    notes that, if the input is array data structure, constraints will be joined using "AND" (case 1),
    otherwise, "OR" (case 2)

    case 3 will be converted to ["A = 'B'", "C = 'D'"] aka 'where A = "B" and C = "D"'
    """
    assert (
        iterable(constraints) or type(constraints) is dict
    ), "constraints is supposed to be iterable or a dict."

    if type(constraints) is dict:
        constraints = [
            "{column} = {value}".format(column=k, value=wrap(v))
            for k, v in constraints.items()
        ]

    if len(constraints) == 0:
        return ""

    if len(constraints) == 1:
        return _template.format(constraints=constraints[0])

    return _template.format(constraints=_logical_join(constraints))
