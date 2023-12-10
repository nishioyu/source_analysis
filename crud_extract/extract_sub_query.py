# サブクエリ含まれるか判定処理
def contains_select_substring(input_string):
    return "(SELECT" in input_string

def remove_outer_parentheses(input_string):
    while input_string.startswith("(") and input_string.endswith(")"):
        input_string = input_string[1:-1]
    return input_string

# サブクエリリスト作成処理
def extract_subqueries(sql_query):
    subqueries = []
    stack = []
    
    for char in sql_query:
        if char == '(':
            if ''.join(stack).endswith('SELECT'):
                stack = [char]  # 新しいサブクエリの開始
            else:
                stack.append(char)
        elif char == ')':
            stack.append(char)
            if stack.count('(') == stack.count(')'):
                # "("と")"の数が一致したらサブクエリを結合してリストに追加
                subquery = ''.join(stack)
                subqueries.append(subquery)
                stack = []  # スタックを空にする
        elif stack:
            stack.append(char)
    
    result_list = [item[1:-1] if item.startswith("(") and item.endswith(")") else item for item in subqueries]
    result_list = [remove_outer_parentheses(x) for x in result_list if "SELECT" in x]
    return result_list

def process_sql_queries(sql_query_list):
    result_list = []

    for sql_query in sql_query_list:
        if contains_select_substring(sql_query):
            subqueries = extract_subqueries(sql_query)
            result_list.extend(subqueries)

    return result_list


def create_sub_queries_list(sql_query):
    result_list = []
    tmp_list = []
    tmp_list.append(sql_query)
    while len(tmp_list) != 0:
          result_list.extend(tmp_list)
          tmp_list = process_sql_queries(tmp_list)
    return result_list


