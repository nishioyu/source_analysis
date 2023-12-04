from sql_metadata import Parser
import re

# SELECTのSQLから最外部に当たるCRUDを抽出する処理
def r_extract_crud(sql_query):
    # SQL文をパースして追加
    parse = Parser(sql_query)

    # テーブル名の取得処理
    # FROM句のテーブル名をエイリアス含めて取得、エイリアスがない場合はテーブルフルネームをエイリアスとする
    # エイリアス付きのテーブルを辞書型で抽出する. ただしkeyが"JOIN","ON","GRUP BY","LEFT JOIN","INNER JOIN","RIGHT JOIN","FULL OUTER JOIN"があるものは考えない. サブクエリの中のテーブルも抽出される
    # エイリアスがある最外部のテーブル名とエイリアスがないテーブル名をエイリアスに自身の名称をつけて結合する.
    tables_list = parse.tables
    tables_list_no_ailiases = dict(zip(tables_list,tables_list))
    tables_list_ailiases = parse.tables_aliases
    # print(tables_list_no_ailiases)
    # print(tables_list_ailiases)
    tables_dict = {**dict(zip(tables_list,tables_list)), **parse.tables_aliases}

    # カラム名を取得、カラム名をエイリアス付きで取得し、エイリアスがない場合にはカラム名本名をエイリアスに指定する
    columns_list = parse.columns_dict["select"]
    columns_list_no_ailiases = [x for x in columns_list if "." not in x]
    columns_list_ailiases = [x for x in columns_list if "." in x]

    # print(columns_list_no_ailiases)
    # print(columns_list_ailiases)

    return_list = []
    # カラム名にエイリアスがあればエイリアスに対応するテーブルの辞書のリストに追加する
    # カラム名にエイリアスがなければ、エイリアスがないテーブルのリストの最初のテーブルのカラムとして返却する
    if len(tables_list_no_ailiases) == 0:
        return_list.append(("SELECT",tables_list_no_ailiases[0],columns_list_no_ailiases))
    # return "SELECT",tables_list_no_ailiases[0],columns_list_no_ailiases

    for k,v in tables_dict.items():
        return_list.append(("SELECT",v,[y for y in columns_list_ailiases if k in y]))
        # return  "SELECT",x,[y for y in columns_list_ailiases if x in y]

    return return_list

