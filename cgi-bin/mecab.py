#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from flask import Flask, jsonify, abort, make_response
import json
import MeCab

form = cgi.FieldStorage()
course_name = form.getvalue('say', '')

mecab = MeCab.Tagger("-Ochasen")
result = mecab.parse(course_name)
clazz = result.split()
if clazz[0] != 'EOS':
    result = {
        "result":True,
        "data":{
            "文法":clazz[3]
    }
    }
    print('Content-type: text/html; charset=UTF-8\r\n')
    print(result)
