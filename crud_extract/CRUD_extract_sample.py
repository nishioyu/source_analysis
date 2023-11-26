
import re

def parse_sql(sql):
    # 正規表現を使用して基本的なSQL文の解析
    select_pattern = re.compile(r'\bSELECT\b.*\bFROM\b\s*([a-zA-Z_][a-zA-Z0-9_]*)', re.IGNORECASE)
    insert_pattern = re.compile(r'\bINSERT INTO\b\s*([a-zA-Z_][a-zA-Z0-9_]*)', re.IGNORECASE)
    update_pattern = re.compile(r'\bUPDATE\b\s*([a-zA-Z_][a-zA-Z0-9_]*)', re.IGNORECASE)
    delete_pattern = re.compile(r'\bDELETE FROM\b\s*([a-zA-Z_][a-zA-Z0-9_]*)', re.IGNORECASE)

    select_match = select_pattern.search(sql)
    insert_match = insert_pattern.search(sql)
    update_match = update_pattern.search(sql)
    delete_match = delete_pattern.search(sql)

    # CRUDの判定
    if select_match:
        crud = "SELECT"
    elif insert_match:
        crud = "INSERT"
    elif update_match:
        crud = "UPDATE"
    elif delete_match:
        crud = "DELETE"
    else:
        crud = "UNKNOWN"

    # テーブルの取得
    table = select_match.group(1) if select_match else \
            insert_match.group(1) if insert_match else \
            update_match.group(1) if update_match else \
            delete_match.group(1) if delete_match else \
            "UNKNOWN"

    # カラムの取得
    columns = re.findall(r'\b(?:SELECT|INSERT INTO)\b\s*(.*?)\s*\bFROM\b|\bUPDATE\b\s*.*\bSET\b\s*(.*?)\s*\bWHERE\b|\bDELETE FROM\b\s*.*\bWHERE\b|\bVALUES\b\s*\((.*?)\)', sql, re.IGNORECASE)
    columns = [column.strip() for column in columns[0] if column]

    return crud, table, columns

# テスト用のSQL文
sql_query = "SELECT column1, column2 FROM table WHERE condition"
sql_insert = "INSERT INTO table (column1, column2) VALUES (value1, value2)"
sql_update = "UPDATE table SET column1 = value1, column2 = value2 WHERE condition"
sql_delete = "DELETE FROM table WHERE condition"

# 解析の実行と結果の出力
crud, table, columns = parse_sql(sql_query)
print(f"CRUD: {crud}\nTable: {table}\nColumns: {columns}\n")

crud, table, columns = parse_sql(sql_insert)
print(f"CRUD: {crud}\nTable: {table}\nColumns: {columns}\n")

crud, table, columns = parse_sql(sql_update)
print(f"CRUD: {crud}\nTable: {table}\nColumns: {columns}\n")

crud, table, columns = parse_sql(sql_delete)
print(f"CRUD: {crud}\nTable: {table}\nColumns: {columns}\n")
