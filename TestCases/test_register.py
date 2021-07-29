
import unittest
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.myddt import ddt, data
from Common.handle_db import HandleDB
from Common.handle_log import logger
from Common.handle_phone import get_new_phone
from Common.handle_data import replace_data
from Common.handle_requests import send_requests

get_excel = HandleExcel(datas_dir+"/api_cases.xlsx","注册")
cases = get_excel.read_all_datas()
get_excel.close_file()
db = HandleDB()

@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("***************************注册用例开始*****************************************")

    @classmethod
    def tearDownClass(cls):
        logger.info("***************************注册用例结束*****************************************")

    @data(*cases)
    def test_register(self,case):
        logger.info("***************执行第{}条用例：{}*********************".format(case["id"], case["title"]))

        if case["request_data"].find("#phone#") != -1:
            new_phone = get_new_phone()
            case = replace_data(case,"#phone#", new_phone)
        resp = send_requests(case["method"],case["url"],case["request_data"])
        expected = eval(case["expected"])
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            self.assertEqual(resp.json()["code"],expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])
            # 数据库校验
            if case["check_sql"]:
                result = db.select_one_data(case["check_sql"])
                self.assertIsNotNone(result)
        except AssertionError as e:
            logger.exception("断言失败!")
            raise e





