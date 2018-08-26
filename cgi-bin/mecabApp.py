#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from flask import Flask, jsonify, abort, make_response
import json
import MeCab

api = Flask(__name__)

# GETの実装
@api.route('/<string:users>', methods=['GET'])
def get_user(users):
    print(users)
    mecab = MeCab.Tagger("-Ochasen")
    result = mecab.parse(users)
    clazz = result.split()
    if clazz[0] != 'EOS':
        result = {
            "result":True,
            "data":{
                "文法":clazz[3]
        }
    }
    return make_response(json.dumps(result, ensure_ascii=False,indent=2))
    print('Content-type: text/html; charset=UTF-8\r\n')
    print(result)
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8000)
