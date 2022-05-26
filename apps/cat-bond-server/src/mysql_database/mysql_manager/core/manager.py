import logging

import numpy as np
from loguru import logger

from mysql_database.mysql_manager.helpers.checkers import iterable
from mysql_database.mysql_manager.queries import wrap
from mysql_database.mysql_manager.queries.select_ import (select_query,
                                                          select_where_query)


def close(conn, cursor):
    """
    A method used to close connection of mysql.
    """
    cursor.close()
    conn.close()


class MySQLManager:
    def __init__(self, connection_pool):
        self.cnx_pool = connection_pool

    def do(self, query, debug=False):
        if debug:
            logger.info(query)
            return

        conn = self.cnx_pool.get_connection()
        cursor = conn.cursor(buffered=True)
        try:
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            logger.error("method 'do' failed: {}".format(e))
            close(conn, cursor)
            return False
        close(conn, cursor)
        return True

    def grab(self, table):
        return self.fetch(select_query(table=table))

    def fetch(self, query, only_first_row=False):
        conn = self.cnx_pool.get_connection()
        cursor = conn.cursor(buffered=True)
        try:
            cursor.execute(query)
            got = cursor.fetchall()
            got = np.array(got).tolist()
            close(conn, cursor)
            if only_first_row:
                return got[0]
            return got
        except Exception as e:
            print("method 'fetch' failed: {}".format(e))
            close(conn, cursor)

    def fetch_vals(self, query):
        return self.fetch(query)[0]

    def fetch_a_val(self, query):
        return self.fetch(query)[0][0]

    def fetch_the_val(self, table, target_col, constraints, all=False):
        got = self.fetch(
            select_where_query(table=table, columns=target_col, constraints=constraints)
        )
        if all:
            return got
        return got[0][0]

    def fetch_the_row(self, table, target_columns, constraints):
        got = self.fetch(
            select_where_query(
                table=table, columns=target_columns, constraints=constraints
            )
        )
        return got[0]

    def count(self, table, constraints=None):
        if constraints is None:
            return self.fetch(select_where_query(table=table, columns=["COUNT(*)"]))[0][
                0
            ]
        assert iterable(constraints), "constraints is supposed to be iterable."
        return self.fetch_a_val(
            select_where_query(
                table=table, columns=["COUNT(*)"], constraints=constraints
            )
        )

    def count_by_columns(self, table, constraints):
        assert (
            type(constraints) is dict
        ), 'constraints is supposed to be a dict, e.g. {"column1": "str_val1", "column2": int_val2}'
        constraints = [
            "{column} = {value}".format(column=k, value=wrap(v))
            for k, v in constraints.items()
        ]
        return self.count(table, constraints=constraints)

    def drop(self, table):
        self.do("DROP TABLE {table}".format(table=table))

    def drain(self, table):
        self.do("DELETE FROM {table}".format(table=table))

    def find_tbl_primary_keys(self, table):
        """returns a two-dimensional array, e.g. [[pk1],[pk2],[[k3]]"""
        return self.fetch(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tbl_name}' AND COLUMN_KEY = 'PRI';".format(
                tbl_name=table
            )
        )
