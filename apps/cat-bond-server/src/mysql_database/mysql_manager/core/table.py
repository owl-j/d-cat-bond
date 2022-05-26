from mysql_database.mysql_manager.helpers.checkers import iterable
from mysql_database.mysql_manager.queries.create import create_query


class Table:
    def __init__(self, tbl_name, fields):
        """
        tbl_name: table A
        fields: [(col1, VARCHAR(255)), (col2, BOOLEAN)...]
        """
        self.tbl_name = tbl_name
        assert iterable(
            fields
        ), "fields supposed to be iterable, e.g. [(col1, VARCHAR(255)), (col2, BOOLEAN)...]"
        self.fields = fields
        self.comments = ""

    @property
    def columns(self):
        return [field[0] for field in self.fields]

    def indexed_columns(self):
        return {i: field_with_type[0] for i, field_with_type in enumerate(self.fields)}

    @property
    def primary_keys(self):
        return [field[0] for field in self.fields if "PRIMARY KEY" in field[1]]

    @property
    def non_auto_incremental_fields(self):
        return [field[0] for field in self.fields if "AUTO_INCREMENT" not in field[1]]

    @property
    def non_auto_incremental_fields_camel(self):
        return [
            "".join(
                [field[0].split("_")[0]]
                + [
                    ele[0].upper() + ele[1:]
                    for i, ele in enumerate(field[0].split("_")[1:])
                ]
            )
            for field in self.fields
            if "AUTO_INCREMENT" not in field[1]
        ]

    @property
    def create_query(self):
        return create_query(
            table_name=self.tbl_name,
            column_names_and_definitions=self.fields,
        )

    def this_column_index(self, col):
        return self.columns.index(col)

    def row_dict(self, row, to_js_syntax=False):
        assert len(row) == len(
            self.fields
        ), "row_dict func only works when the number of the row exactly matches how many fields this table has."
        if to_js_syntax:
            return {
                "".join(
                    [key.split("_")[0]]
                    + [
                        ele[0].upper() + ele[1:]
                        for i, ele in enumerate(key.split("_")[1:])
                    ]
                ): value
                for (key, value) in zip(self.columns, row)
            }
        return {key: value for (key, value) in zip(self.columns, row)}

    def add_table_comments(self, comments):
        self.comments = comments

    def get_table_comments(self):
        return self.comments
