# -*- coding: utf-8 -*-
from branch.log import Log
logger = Log()


def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1 = ([(str(fanhuijson[key])) for key in result.keys()])
        value2 = ([(str(value)) for value in result.values()])
        if value1 == value2:
            return {'code': 0, "result": 'pass'}
        else:
            return {'code': 1, 'result': 'fail'}
    else:
        Log().info('填写测试预期值')
        return {"code": 2, 'result': '填写测试预期值'}

def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')   #['code=4001']
        result = dict([(item.split('=')) for item in data])    #{'code': '4001'}
        return result
    else:
        Log().info('填写测试预期值')
        raise {"code": 1, 'result': '填写测试预期值'}

