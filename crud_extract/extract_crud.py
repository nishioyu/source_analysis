import get_sql_operation_type
import r_extract_crud
# import crud_extract.c_extract_crud as c_extract_crud
import create_sub_queries_list
from itertools import chain


# CRUD抽出処理
def extract_crud(sql_query):
    target_list = create_sub_queries_list(sql_query)
    if target_list[0] == "R":
        tmp_list = map(r_extract_crud,target_list)
        flattened_tmp_list = list(chain(*tmp_list))
        return flattened_tmp_list
    # None



# from collections import defaultdict

# def aggregate_tuples(tuple_list):
#     # デフォルト値がセットの辞書を用意
#     result_dict = defaultdict(set)

#     # タプルのリストを処理して辞書に追加
#     for tup in tuple_list:
#         key = (tup[0], tup[1])
#         result_dict[key].add(tup[2])

#     # 新しいタプルのリストを作成
#     result_list = [(key[0], key[1], set_values) for key, set_values in result_dict.items()]

#     return result_list

# # テスト
# original_tuple_list = [(1, 2, 'a'), (1, 2, 'b'), (3, 4, 'c'), (3, 4, 'd'), (5, 6, 'e')]
# result = aggregate_tuples(original_tuple_list)
# print(result)
