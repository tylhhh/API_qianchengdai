import unittest
import json
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.myddt import ddt,data
from Common.handle_log import logger
from Common.handle_data import EnvData,clear_EnvData_atts,replace_case_by_regular
from Common.handle_requests import send_requests
from Common.handle_extract_data import extract_data
from Common.handle_db import HandleDB

get_excel = HandleExcel(datas_dir+"/api_cases.xlsx","加标")
cases = get_excel.read_all_datas()
get_excel.close_file()
db = HandleDB()

@ddt
class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("***************************加标用例开始*********************************")
        clear_EnvData_atts()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("***************************加标用例开始*********************************")


    @data(*cases)
    def test_add(self,case):
        logger.info("***************执行第{}条用例：{}*********************".format(case["case_id"], case["title"]))
        replace_case_by_regular(case)
        if hasattr(EnvData,"token"):
            resp = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)
        else:
            resp = send_requests(case["method"], case["url"], case["request_data"])
        if case["extract_data"]:
            extract_data(case["extract_data"],resp.json())
        if case["expected"]:
            expected = eval(case["expected"])
            logger.info("用例的期望结果为：{}".format(expected))
            try:
                self.assertEqual(resp.json()["code"], expected["code"])
                self.assertEqual(resp.json()["msg"], expected["msg"])
                # 数据库校验
                if case["check_sql"]:
                    result = db.select_one_data(case["check_sql"])
                    self.assertIsNotNone(result)
            except AssertionError as e:
                logger.exception("断言失败!")
                raise e
