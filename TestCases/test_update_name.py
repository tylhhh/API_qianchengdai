import unittest
import json
from Common.handle_excel import HandleExcel
from Common.myddt import ddt,data
from Common.handle_path import datas_dir
from Common.handle_log import logger
from Common.handle_requests import send_requests
from Common.handle_data import replace_case_by_regular,EnvData,clear_EnvData_atts
from Common.handle_phone import get_old_phone
from jsonpath import jsonpath


get_excel = HandleExcel(datas_dir+"/api_cases.xlsx","更新昵称")
cases = get_excel.read_all_datas()
get_excel.close_file()


@ddt
class TestUpdate(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("****************************登录前置*******************************")
        clear_EnvData_atts()  # 清理EnvData里设置的属性
        user, passwd = get_old_phone()
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": passwd})
        setattr(EnvData, "member_id", jsonpath(resp.json(), "$..id")[0])
        setattr(EnvData, "token", jsonpath(resp.json(), "$..token")[0])

    def tearDown(self) -> None:
        logger.info("****************************更新用户信息用例结束*******************************")

    @data(*cases)
    def test_update(self,case):
        logger.info("***************执行第{}条用例：{}*********************".format(case["case_id"], case["title"]))
        if case["request_data"].find("#member_id#") != -1:
            case = replace_case_by_regular(case)
        resp = send_requests(case["method"],case["url"],case["request_data"], token=EnvData.token)
        expected = json.loads(case["expected"])
        logger.info("用例的期望结果为：{}".format(expected))
        try:
            self.assertEqual(resp.json()["code"], expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])
        except AssertionError as e:
            logger.exception("断言失败!")
            raise e




