_template1 = "CREATE VIEW {view_name} AS {select_statement};"


def create_view_query_by_select_statement(view_name, select_statement):
    return _template1.format(view_name=view_name, select_statement=select_statement)
