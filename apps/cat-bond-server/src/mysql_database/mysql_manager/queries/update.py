from mysql_database.mysql_manager.helpers.checkers import \
    iterable_and_not_string
from mysql_database.mysql_manager.queries import wrap
from mysql_database.mysql_manager.queries.where import where

_template1 = "UPDATE {table} SET {target_column}={target_value} WHERE {base_column}={base_value};"
_template2 = (
    "UPDATE {table} SET {target_columns_and_values} WHERE {base_column}={base_value};"
)
_template3 = "UPDATE {table} SET {target_column}={target_value} {where};"
_template4 = "UPDATE {table} SET {target_columns_and_values} {where};"


def _process_wrapping_target_val(target_val, wrap_target_val):
    if wrap_target_val:
        return wrap(target_val)
    return target_val


def construct_target_columns_and_values(columns_and_values, wrap_target_val=None):
    """
    wrap_target_val is supposed to be iterable:

    the length is the same as columns_and_values
    meanwhile each bool in wrap_target_val indicating if we wrap or not wrap the target val in columns_and_values
    """
    if wrap_target_val is None:
        wrap_target_val = [True for _ in range(len(columns_and_values))]

    assert iterable_and_not_string(
        columns_and_values
    ), "columns_and_values supposed to be iterable, e.g. [('col1', 'val1'), ('col2', val2)]"

    assert iterable_and_not_string(
        wrap_target_val
    ), "wrap_target_val is supposed to be iterable."

    assert len(columns_and_values) == len(
        wrap_target_val
    ), "length of columns_and_values array is supposed to be the same as wrap_target_val array"

    return ", ".join(
        [
            "{column}={value}".format(
                column=str(item[0]),
                value=_process_wrapping_target_val(
                    target_val=item[1], wrap_target_val=wrap_target_val[i]
                ),
            )
            for i, item in enumerate(columns_and_values)
        ]
    )


def update_query_single_column(
    table_name, target_col, target_val, base_col, base_val, wrap_target_val=True
):
    return _template1.format(
        table=table_name,
        target_column=target_col,
        target_value=_process_wrapping_target_val(target_val, wrap_target_val),
        base_column=base_col,
        base_value=wrap(base_val),
    )


def update_query_multi_columns(
    table_name, columns_and_values, base_col, base_val, wrap_target_val=None
):
    return _template2.format(
        table=table_name,
        target_columns_and_values=construct_target_columns_and_values(
            columns_and_values, wrap_target_val
        ),
        base_column=base_col,
        base_value=wrap(base_val),
    )


def update_query_single_column_where_constrained(
    table_name, target_col, target_val, constraints, wrap_target_val=True
):
    return _template3.format(
        table=table_name,
        target_column=target_col,
        target_value=_process_wrapping_target_val(target_val, wrap_target_val),
        where=where(constraints),
    )


def update_query_multi_columns_where_constrained(
    table_name, columns_and_values, constraints, wrap_target_val=None
):
    return _template4.format(
        table=table_name,
        target_columns_and_values=construct_target_columns_and_values(
            columns_and_values, wrap_target_val
        ),
        where=where(constraints),
    )
