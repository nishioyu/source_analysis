# CRUD抽出処理
## 概要
与えられたSQL文（Python文字列形式）から、CRUDを抽出する処理を作成.
入力SQL文はSELECT,INSERT,UPDATE,DELETE文を想定.またSQL文は一つのSQL文が入力として与えられる想定である.
出力形式はタプルのリスト形式で、各タプルは(CRUD形式:Python文字列, テーブル名:Python文字列, カラム名の集合:Pythonのset型)で与えられる. 

## 使い方
crud_extract/extract_crud.py　の中のextract_crud関数にSQL文を与えることで実行することができる.

## その他関数や機能の紹介
xxxx

## 今後対応する機能
xxxx
