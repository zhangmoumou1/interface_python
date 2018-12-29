import os
import time
import unittest
from branch import HTMLTestReportCN
from config import globalparam

test_dir = "./testCase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*case.py")

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
#     now = time.strftime("%Y-%m-%d %H-%M-%S")
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     file_dir = os.path.join(basedir, 'test_Report')
#     filename = globalparam.report_path + "\\" + now + "result.html"
#     re_open = open(filename, 'wb')
#     runner = BSTestRunner.BSTestRunner(stream=re_open, title='http接口测试报告', description='测试结果')
#     m=runner.run(suite)
if __name__ == "__main__":
    # Get the current time in a certain format
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # Define the report storage path
    filename = globalparam.report_path + "/" + "result.html"
    fp = open(filename, 'wb')
    #runner = BSTestRunner.BSTestRunner(stream=fp, title='http接口测试报告', description='测试结果')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        # description='详细测试用例结果',    #不传默认为空
        tester=u"命命"  # 测试人员名字，不传默认为QA
    )
    runner.run(discover)
    fp.close()
