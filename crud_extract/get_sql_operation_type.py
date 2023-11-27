import re

# 最外部CRUD判定処理
def get_sql_operation_type(sql_query):
    # 正規表現を使用して最初のキーワードを抽出
    match = re.search(r'\b(SELECT|INSERT|UPDATE|DELETE)\b', sql_query, re.IGNORECASE)

    if match:
        keyword = match.group(1).upper()

        # 対応する操作タイプを返す
        if keyword == "SELECT":
            return "R"
        elif keyword == "INSERT":
            return "C"
        elif keyword == "UPDATE":
            return "U"
        elif keyword == "DELETE":
            return "D"

    # 対応するキーワードが見つからない場合は None を返す
    return None