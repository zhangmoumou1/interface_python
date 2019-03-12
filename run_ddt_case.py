import os
import time
import unittest
from Branch import HTMLTestReportCN
from config import globalparam

test_dir = "./testcase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*case.py")

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = globalparam.report_path + "/" + "result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        # description='详细测试用例结果',    #不传默认为空
        tester=u"命命"  # 测试人员名字，不传默认为QA
    )
    runner.run(discover)
    fp.close()
