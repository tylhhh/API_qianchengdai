
import unittest
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.myddt import ddt, data
from Common.handle_db import HandleDB
from Common.handle_log import logger
from Common.handle_requests import send_requests

get_excel = HandleExcel(datas_dir+"/api_cases.xlsx","登陆")
cases = get_excel.read_all_datas()
get_excel.close_file()
db = HandleDB()

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("***************************登录用例开始*****************************************")

    @classmethod
    def tearDownClass(cls):
        logger.info("***************************登录用例结束*****************************************")

    @data(*cases)
    def test_login(self,case):
        logger.info("***************执行第{}条用例：{}*********************".format(case["id"], case["title"]))

        resp = send_requests(case["method"],case["url"],case["request_data"])
        expected = eval(case["expected"])
        logger.info("用例的期望结果为：{}".format(expected))
        try:
            self.assertEqual(resp.json()["code"],expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])
        except AssertionError as e:
            logger.exception("断言失败!")
            raise e





