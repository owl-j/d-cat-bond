from mysql_database.mysql_manager.helpers.checkers import \
    iterable_list_of_tup_pairs

_template1 = "ALTER TABLE {table_name} ADD {column_name} {datatype};"
_template2 = "ALTER TABLE {table_name} ADD COLUMN {column_name} {datatype} AFTER {the_col_after_name};"
_template3 = "ALTER TABLE {table_name} DROP COLUMN {column_name};"
_template4 = "ALTER TABLE {table_name} MODIFY COLUMN {column_name} {datatype};"


def query_update_column_datatype(table_name, column_name, datatype):
    return _template1.format(
        table_name=table_name, column_name=column_name, datatype=datatype
    )


def query_drop_a_column(table_name, column_name):
    return _template3.format(table_name=table_name, column_name=column_name)


def query_modify_a_column_datatype(table_name, column_name, datatype):
    return _template4.format(
        table_name=table_name, column_name=column_name, datatype=datatype
    )


def queries_modify_columns_datatypes(table_name, columns_datatypes):
    assert iterable_list_of_tup_pairs(
        columns_datatypes
    ), "columns_datatypes not iterable or list of tuples of length 2"
    return [
        query_modify_a_column_datatype(
            table_name=table_name,
            column_name=column_datatype[0],
            datatype=column_datatype[1],
        )
        for column_datatype in columns_datatypes
    ]


def query_append_column_to_tbl(
    column_name_datatype_tuple, tbl_name, the_col_after_name
):
    return _template2.format(
        table_name=tbl_name,
        column_name=column_name_datatype_tuple[0],
        datatype=column_name_datatype_tuple[1],
        the_col_after_name=the_col_after_name,
    )
