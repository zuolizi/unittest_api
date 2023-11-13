from lib.HTMLTestRunnerNew import HTMLTestRunner
from utils.handle_path import *
import unittest
import time

current_time = time.strftime('%Y-%m-%d %H-%M-%S')
report_file = report_path + '\\' + "api_report" + current_time + '.html'


def run_allcase():
    #  def discover(self, start_dir, pattern='test*.py', top_level_dir=None):
    unittest.TestSuite()
    suite = unittest.defaultTestLoader.discover(start_dir=testcase_path)
    f = open(report_file, 'wb')
    # def __init__(self, stream=sys.stdout, verbosity=2, title=None, description=None, tester=None):
    HTMLTestRunner(
        stream=f,
        title='接口自动化测试报告',
        description='执行情况如下：',
        tester='左治权'
    ).run(suite)
    f.close()


if __name__ == '__main__':
    run_allcase()
