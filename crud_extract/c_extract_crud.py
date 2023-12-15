import re
import re

def replace_whitespace(input_string):
    # 任意の空白文字（スペース、タブ、改行など）を半角スペースに置換
    result_string = re.sub(r'\s+', ' ', input_string)
    return result_string

def extract_insert_values(sql_query):
    # INSERT文の正規表現パターン
    sql_query = replace_whitespace(sql_query.replace("\n", " "))
    pattern = re.compile(r"INSERT\s+INTO\s+(.*?)\s+VALUES")

    # パターンにマッチする部分を検索
    match = pattern.search(sql_query)

    if match:
        # テーブル名を取得
        result = match.group(1)
        return result
    else:
        return None

def process_string(input_string):
    # 最初に登場する半角スペースより前の文字列を抽出
    match_space = re.match(r'^\s*([^ ]+)', input_string)
    first_element = match_space.group(1) if match_space else ""

    # "("と")"の間の文字列を抽出
    match_parentheses = re.search(r'\((.*?)\)', input_string)
    second_element = set(match_parentheses.group(1).split(',')) if match_parentheses else {"*"}

    return first_element, second_element
    
def c_extract_crud(sql_query):
    tmp = extract_insert_values(sql_query)
    result = process_string(tmp)
    return result