import unittest

import ddt

from Public.expect import assertre
from Public.select_request import TestApi
from branch.get_excel import makedata
from branch.log import Log

data_test = makedata()

@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        Log().info('测试用例开始执行')

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

    @ddt.data(*data_test)
    def testCase(self, data_test):
        expect_one = dict(assertre(asserqingwang=data_test['expect1']))
        expect_two = dict(assertre(asserqingwang=data_test['expect2']))
        data1 = list(expect_two.keys())[0]  #传递给实际值所要的key值，如task
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url=data_test['url'], key=data_test['key'], connent=data_test['coneent'],
                          fangshi=data_test['fangshi'],assertdata=data1,param_place=data_test['param_place']).testapi()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                         data_test['coneent'], data_test['fangshi']))
        #apijson = dict(api.getJson())
        # Log().info('返回实际结果:%s' % apijson)
        try:
            self.assertEqual(int(expect_one['code']), apijson[0], msg='预期和返回不一致')
            Log().info('对【code】断言,断言结果--预期值%s == 实际值%s' % (expect_one['code'], apijson[0]))
        except:
            Log().warning('对【code】断言,断言结果--预期值%s != 实际值%s' % (expect_one['code'], apijson[0]))
            raise
        if data1 != "param":
            try:
                self.assertEqual(expect_two[data1], apijson[1], msg='预期和返回不一致')
                Log().info('对【%s】字段断言,断言结果--预期值%s == 实际值%s' % (data1, expect_two[data1], apijson[1]))
            except:
                Log().warning('对【%s】字段断言,断言结果--预期值%s != 实际值%s' % (data1, expect_two[data1], apijson[1]))
                raise

if __name__ == "__main__":
    unittest.main()
