from sql_metadata import Parser
import re

# # 最外部のSELECT文のカラム名を抽出する処理
# def extract_columns_from_select(sql_query):
#     # SELECTからFROMまでの部分を正規表現で抽出
#     match = re.search(r'\bSELECT\b(.*?)(\bFROM\b|$)', sql_query, re.DOTALL | re.IGNORECASE)
#     if match:
#         select_part = match.group(1).strip()
#         # カンマで分割してリストにする
#         columns = [col.strip() for col in select_part.split(',')]
#         return columns
#     return None

# SELECTのSQLから最外部に当たるCRUDを抽出する処理
def r_extract_crud(sql_query):
    parse = Parser(sql_query)
    # テーブル名の取得処理
    # FROM句のテーブル名をエイリアス含めて取得、エイリアスがない場合はテーブルフルネームをエイリアスとする
    # エイリアス付きのテーブルを辞書型で抽出する. ただしkeyが"JOIN","ON","GRUP BY","LEFT JOIN","INNER JOIN","RIGHT JOIN","FULL OUTER JOIN"があるものは考えない. サブクエリの中のテーブルも抽出される
    # エイリアスがある最外部のテーブル名とエイリアスがないテーブル名をエイリアスに自身の名称をつけて結合する.
    tables_list = parse.tables
    tables_dict = {**dict(zip(tables_list,tables_list)), **parse.tables_aliases}
    # カラム名を取得、カラム名をエイリアス付きで取得し、エイリアスがない場合にはカラム名本名をエイリアスに指定する
    columns_list = parse.columns_dict["select"]

    # カラム名のエイリアスがない場合はFROM句のテーブルを辞書にもつリストに、
    # カラム名にエイリアスがあればエイリアスに対応するテーブルの辞書のリストに追加する
    # SELECT,テーブル名,テーブルに属するカラム名のリスト　の組みをテーブル毎に返却する
    return None