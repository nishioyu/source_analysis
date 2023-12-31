import get_sql_operation_type
import r_extract_crud
import c_extract_crud
import create_sub_queries_list
from itertools import chain
from collections import defaultdict

# import crud_extract.c_extract_crud as c_extract_crud
def aggregate_tuples(tuple_list):
    # デフォルト値がセットの辞書を用意
    result_dict = defaultdict(set)

    # タプルのリストを処理して辞書に追加
    for tup in tuple_list:
        key = (tup[0], tup[1])
        result_dict[key] = result_dict[key].union(set(tup[2]))
    # 新しいタプルのリストを作成
    result_list = [(key[0], key[1], set_values) for key, set_values in result_dict.items()]

    return result_list


# CRUD抽出処理 (CRUD,TBL名,{カラムの集合})のリストの形式で出力する　
def extract_crud(sql_query):
    target_list = create_sub_queries_list(sql_query)

    if get_sql_operation_type(target_list[0]) == "R":
        tmp_list = map(r_extract_crud,target_list)
        flattened_tmp_list = list(chain(*tmp_list))
        result = aggregate_tuples(flattened_tmp_list) # テーブルごとに要素をマージする処理
        return result
    
    if get_sql_operation_type(target_list[0]) == "C":
        tmp_list_1 = [c_extract_crud(("INSERT",target_list[0])[0],c_extract_crud(target_list[0])[1])] 
        tmp_list_2 = []
        if len(target_list) > 1:
            tmp_list = map(r_extract_crud,target_list[1:])
            flattened_tmp_list = list(chain(*tmp_list))
            temp_list_2 = aggregate_tuples(flattened_tmp_list) # テーブルごとに要素をマージする処理
        result = tmp_list_1 + tmp_list_2
        return result
    
    if get_sql_operation_type(target_list[0]) == "U":
        # tmp_list = map(u_extract_crud,target_list)
        # flattened_tmp_list = list(chain(*tmp_list))
        # return aggregate_tuples(flattened_tmp_list)
        return None
    
    if get_sql_operation_type(target_list[0]) == "D":
        # tmp_list = map(d_extract_crud,target_list)
        # flattened_tmp_list = list(chain(*tmp_list))
        # return aggregate_tuples(flattened_tmp_list)
        return None
    





