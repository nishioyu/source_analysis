from sql_metadata import Parser
import re

def extract_first_select_columns_from_sql(sql_query):
    # SQL文からSELECTとFROMの間の部分を正規表現で抽出
    match = re.search(r'SELECT(.*?)FROM', sql_query, re.DOTALL)
    
    if match:
        # 抽出した部分からカラムを取得
        selected_part = match.group(1).strip()
        
        # カンマで分割してリストに格納
        columns = [column.strip() for column in selected_part.split(',')]
        return columns
    else:
        # SELECTとFROMが見つからない場合はエラー処理などを行うことも考慮できます
        return None

# SELECTのSQLから最外部に当たるCRUDを抽出する処理
def r_extract_crud(sql_query):
    parse = Parser(sql_query)

    tables_list = parse.tables
    tables_list_no_ailiases = dict(zip(tables_list,tables_list))
    # エイリアス付きのテーブルを辞書型で抽出する. ただしkeyが
    # "JOIN","ON","GRUP BY","LEFT JOIN","INNER JOIN","RIGHT JOIN","FULL OUTER JOIN"
    # があるものは考えない. サブクエリの中のテーブルも抽出される
    tables_list_ailiases = parse.tables_aliases
    tables_dict = {**dict(zip(tables_list,tables_list)), **parse.tables_aliases}

    # columns_list = parse.columns_dict["select"]
    columns_list = extract_first_select_columns_from_sql(sql_query)

    columns_list_no_ailiases = [x for x in columns_list if "." not in x]
    columns_list_ailiases = [x for x in columns_list if "." in x]

    print(columns_list_no_ailiases)
    print(columns_list_ailiases)

    return_list = []

    # エイリアスなしカラム用
    if len(list(tables_list_no_ailiases)) != 0:
      for x in tables_list_no_ailiases:
        return_list.append(("SELECT",list(tables_list_no_ailiases)[0],columns_list_no_ailiases))

    # エイリアスありカラム用
    for k,v in tables_dict.items():
        tmp_list = [y for y in columns_list_ailiases if k == y.split(".")[0]]
        if len(tmp_list) != 0:
          return_list.append(("SELECT",v,[y for y in columns_list_ailiases if k == y.split(".")[0]]))

    return return_list

