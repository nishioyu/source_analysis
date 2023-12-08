import get_sql_operation_type
import r_extract_crud
import crud_extract.c_extract_crud as c_extract_crud

# CRUD抽出処理
def extract_crud(sql_query):
    if get_sql_operation_type(sql_query) == "R":
        # R CRUD抽出処理
        r_extract_crud(sql_query)
        # サブクエリリスト作成
        # サブクエリリスト文RCRUD抽出処理

    else:
        # c_extract_crud(sql_query)
        # u_extract_crud(sql_query)
        # d_extract_crud(sql_query)
        None

