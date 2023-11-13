from utils.handle_path import *
from utils.handle_conf import Handle_Conf
from utils.handle_excel import Handle_Excel
from utils.handle_requests import Send_Request
from utils.handle_cms import Handel_CMS
import unittest
from ddt import ddt,data
import warnings

@ddt
class Add_User(unittest.TestCase):
    # 获取config.ini 和 data.xlsx路径
    data_path = os.path.join(data_path, 'data.xlsx')
    # 获取data.xlsx文件的数据
    he = Handle_Excel(data_path, 'adduser')
    datas = he.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        Handel_CMS().login_cms()

    @data(*datas)
    def test_01_adduser(self,case ):
        method = 'post'
        url = 'http://cms.duoceshi.cn/cms/manage/saveSysUser.do'
        add_data = {'userName': '张三',
                      'userSex': 1,
                      'userMobile': '13522223333',
                      'userEmail': '13522223333@abc.com',
                      'userAccount': 'zhangsan123456789',
                      'loginPwd': '123456',
                      'confirmPwd': '123456'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        response = Send_Request.send(method=method,url=url,data=add_data,headers=headers)
        print(response.text)


if __name__ == '__main__':
    unittest.main()

