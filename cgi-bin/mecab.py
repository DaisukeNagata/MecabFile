#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi

# クエリを取得
form = cgi.FieldStorage()
course_name = form.getvalue('say', '')

import MeCab
mecab = MeCab.Tagger("-Ochasen")
result = mecab.parse(course_name)

clazz = result.split()
print(clazz)
if clazz[0] != 'EOS':
    print('Content-type: text/html; charset=UTF-8\r\n')
    print(clazz[3])
