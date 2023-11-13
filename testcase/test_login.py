from utils.handle_path import *
from utils.handle_conf import Handle_Conf
from utils.handle_excel import Handle_Excel
from utils.handle_requests import Send_Request
import unittest
import warnings
from utils.handle_cms import Handel_CMS
from ddt import ddt, data


@ddt
class Test_Login(unittest.TestCase):
    # 获取config.ini 和 data.xlsx路径
    data_path = os.path.join(data_path, 'data.xlsx')
    # 获取data.xlsx文件的数据
    he = Handle_Excel(data_path, 'login')
    datas = he.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    @data(*datas)
    def test_01_login(self, case):
        resp = Handel_CMS().login_cms(case)
        json_resp = resp.json()
        # 响应状态码
        resp_code = json_resp['code']
        # 数据行
        row_num = case['case_id'] + 1
        # 预期状态码
        excepted_code = eval(case['excepted'])['code']
        try:
            self.assertEqual(resp_code,excepted_code)
        except Exception as e:
            print(e)
            self.he.write_data(row=row_num, column=8, value='失败')
        else:
            self.he.write_data(row=row_num, column=8, value='成功')


if __name__ == '__main__':
    unittest.main()
