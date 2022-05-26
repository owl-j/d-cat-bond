from mysql_database.mysql_manager.helpers.checkers import \
    iterable_and_not_string
from mysql_database.mysql_manager.queries import wrap
from mysql_database.mysql_manager.queries.where import where

_template1 = "SELECT {columns} FROM {table};"
_template2 = "SELECT {columns} FROM {table} {where};"
_template3 = "SELECT DISTINCT {columns} FROM {table};"
_template4 = "SELECT DISTINCT {columns} FROM {table} {where};"
_template5 = "SELECT {columns} FROM {table} ORDER BY {orders};"
_template6 = "SELECT {columns} FROM {table} {where} ORDER BY {orders};"
_template7 = "SELECT DISTINCT {columns} FROM {table} ORDER BY {orders};"
_template8 = "SELECT DISTINCT {columns} FROM {table} {where} ORDER BY {orders};"
_template9 = "{select_by_order_query} ASC"
_template10 = "{select_by_order_query} DESC"
_template11 = "{select_query} LIMIT {batch_size} OFFSET {start_index}"


def select_query(table, columns="*", distinct=False):
    if iterable_and_not_string(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template3.format(columns=columns, table=table)
    return _template1.format(columns=columns, table=table)


def select_where_query(table, columns="*", distinct=False, constraints=None):
    if constraints is None:
        constraints = []
    if type(constraints) is dict:
        constraints = [
            "{column} = {value}".format(column=k, value=wrap(v))
            for k, v in constraints.items()
        ]
    if iterable_and_not_string(columns):
        columns = ", ".join(columns)
    if distinct:
        return _template4.format(columns=columns, table=table, where=where(constraints))
    return _template2.format(columns=columns, table=table, where=where(constraints))


def _sort_by_injected_select_by_order_query(select_by_order_query, sort_by):
    if sort_by == "+":
        return _template9.format(
            select_by_order_query=select_by_order_query.replace(";", "")
        )
    if sort_by == "-":
        return _template10.format(
            select_by_order_query=select_by_order_query.replace(";", "")
        )


def select_order_by_query(
    table, columns="*", distinct=False, orders=None, sort_by=None
):
    """
    orders can be the names of some columns

    sort_by can be:
    "+": ASC
    "-": DESC
    """
    if orders is None:
        orders = []
    assert iterable_and_not_string(orders), "orders is supposed to be iterable."
    if iterable_and_not_string(columns):
        columns = ", ".join(columns)

    if distinct:
        select_by_order_query = _template7.format(
            columns=columns, table=table, orders=", ".join(orders)
        )
    else:
        select_by_order_query = _template5.format(
            columns=columns, table=table, orders=", ".join(orders)
        )

    if sort_by is not None:
        return _sort_by_injected_select_by_order_query(
            select_by_order_query=select_by_order_query, sort_by=sort_by
        )
    else:
        return select_by_order_query


def select_where_order_by_query(
    table, columns="*", distinct=False, constraints=None, orders=None, sort_by=None
):
    """
    orders can be the names of some columns

    sort_by can be:
    "+": ASC
    "-": DESC
    """

    if orders is None:
        orders = []
    assert iterable_and_not_string(orders), "orders is supposed to be iterable."

    if constraints is None:
        constraints = []
    if iterable_and_not_string(columns):
        columns = ", ".join(columns)

    if distinct:
        select_by_order_query = _template8.format(
            columns=columns,
            table=table,
            where=where(constraints),
            orders=", ".join(orders),
        )
    else:
        select_by_order_query = _template6.format(
            columns=columns,
            table=table,
            where=where(constraints),
            orders=", ".join(orders),
        )

    if sort_by is not None:
        return _sort_by_injected_select_by_order_query(
            select_by_order_query=select_by_order_query, sort_by=sort_by
        )
    else:
        return select_by_order_query


def slice_select(select_query, start_index, end_index):
    batch_size = int(end_index) - int(start_index)
    if batch_size < 0:
        batch_size = 0
    return _template11.format(
        select_query=select_query.replace(";", ""),
        batch_size=str(batch_size),
        start_index=str(start_index),
    )
