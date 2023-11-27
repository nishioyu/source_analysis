import get_sql_operation_type

# CRUD抽出処理
def extract_crud(sql_query):
    if get_sql_operation_type(sql_query) == "R":
        r_extract_crud(sql_query)
    else:
        cud_sql_query(sql_query)
