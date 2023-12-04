from sql_metadata import Parser
import re

# SELECTのSQLから最外部に当たるCRUDを抽出する処理
def r_extract_crud(sql_query):
    parse = Parser(sql_query)

    tables_list = parse.tables
    tables_list_no_ailiases = dict(zip(tables_list,tables_list))
    tables_list_ailiases = parse.tables_aliases
    # print(tables_list_no_ailiases)
    # print(tables_list_ailiases)
    tables_dict = {**dict(zip(tables_list,tables_list)), **parse.tables_aliases}

    columns_list = parse.columns_dict["select"]
    columns_list_no_ailiases = [x for x in columns_list if "." not in x]
    columns_list_ailiases = [x for x in columns_list if "." in x]

    # print(columns_list_no_ailiases)
    # print(columns_list_ailiases)

    return_list = []
    if len(tables_list_no_ailiases) == 0:
        return_list.append(("SELECT",tables_list_no_ailiases[0],columns_list_no_ailiases))

    for k,v in tables_dict.items():
        return_list.append(("SELECT",v,[y for y in columns_list_ailiases if k == y.split(".")[0]]))

    return return_list

