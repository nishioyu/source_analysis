# update抽出のキモになる部分は何か？
# updateの後には必ずテーブル名がくる. そのあとはSET カラム名達がやってくる.
# カラム名は省略される場合があったり、JOIN句によってテーブルが結合されるケースがある. 


import re 

def u_extract_crud(sql_query):
    return None