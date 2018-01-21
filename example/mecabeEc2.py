#!/usr/bin/python
# -*- coding: utf-8 -*-

# HTTPヘッダ
print ("Content-type: text/html\n")

import cgi

# クエリを取得
form = cgi.FieldStorage()
course_name = form.getvalue('course', '')


import MeCab
mecab = MeCab.Tagger("-Ochasen")
print(mecab.parse(course_name))


# HTML
print ("<html>")
# HTMLヘッダ
print ("<head>")
print ("<title>フォームからのデータ処理のテスト</title>")
print ("</head>")
# HTMLボディ
print ("<body>")
print (course_name)
print ("</body>")
print ("</html>")