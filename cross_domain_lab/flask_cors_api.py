# coding: utf-8
# author: hongxin
# date: 19-04-10

import json
from flask import Flask, request, jsonify, Response
from flask_cors import cross_origin


app = Flask(__name__)


# 通过外部装饰器实现跨域get请求
@app.route('/cd_get_by_decorator', methods=['GET'])
@cross_origin()
def ajax_get_decorator():
    return jsonify({'data': 'ajax'})
    # return json.dumps({'data': 'ajax'})


# 通过设置请求头实现跨域get请求
@app.route('/cd_get_by_header', methods=['GET'])
def ajax_get_header():
    resp = Response(json.dumps({'data': 'ajax'}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


# 通过设置请求头实现跨域post form表单请求
@app.route('/newadmin/PubAdmin.Login', methods=['POST'])
def ajax_post_form_header():
    req = request.form
    print("headers", request.headers)

    # req_json = request.json
    # print("json", req_json)
    # resp = Response(json.dumps(req))
    # resp.headers["Access-Control-Allow-Origin"] = "*"
    # resp.headers["Access-Control-Allow-Methods"] = "GET,POST"
    # resp.headers["Access-Control-Allow-Headers"] = "x-requested-with,content-type"
    return json.dumps({'code': 200, 'data': {'token': '2222'}})


# 通过设置请求头实现跨域post json请求
@app.route('/cd_postJson_by_header', methods=['POST'])
def ajax_post_json_header():
    req = request.json
    print(req)
    resp = Response(json.dumps(req))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6089, debug=True)
