
import unittest,json
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.myddt import ddt, data
from Common.handle_db import HandleDB
from Common.handle_log import logger
from Common.handle_phone import get_new_phone,get_old_phone
from Common.handle_data import replace_data,EnvData,clear_EnvData_atts,replace_case_by_regular
from Common.handle_requests import send_requests
from jsonpath import jsonpath

get_excel = HandleExcel(datas_dir+"/api_cases.xlsx","提现")
cases = get_excel.read_all_datas()
get_excel.close_file()
db = HandleDB()

@ddt
class TestWithdraw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("***************************登录前置*****************************************")
        clear_EnvData_atts()  # 清理EnvData里设置的属性
        user,passwd = get_old_phone()
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": passwd})
        setattr(EnvData, "member_id", jsonpath(resp.json(),"$..id")[0])
        setattr(EnvData, "token", jsonpath(resp.json(), "$..token")[0])

    def tearDown(self) -> None:
        if hasattr(EnvData, "money"):
            delattr(EnvData, "money")

    @data(*cases)
    def test_withdraw(self,case):
        logger.info("***************执行第{}条用例：{}*********************".format(case["case_id"], case["title"]))

        if case["request_data"].find("#member_id#") != -1:
            case = replace_case_by_regular(case)
            # case = replace_data(case,"#member_id#", str(EnvData.member_id))

        if case["check_sql"]:
            withdraw_before_money = db.select_one_data(case["check_sql"])["leave_amount"]
            logger.info("提现前用户余额：{}".format(withdraw_before_money))
            withdraw_money = json.loads(case["request_data"])["amount"]
            logger.info("用户提现的金额:{}".format(withdraw_money))
            expected_money = round(float(withdraw_before_money) - withdraw_money,2)
            logger.info("提现后，期望的金额：{}".format(expected_money))
            # case = replace_data(case, "#money#", str(expected_money))
            setattr(EnvData, "money", str(expected_money))
            case = replace_case_by_regular(case)

        resp = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)
        expected = json.loads(case["expected"])

        try:
            self.assertEqual(resp.json()["code"],expected["code"])
            self.assertEqual(resp.json()["msg"], expected["msg"])
            if case["check_sql"]:
                self.assertEqual(resp.json()["data"]["id"], expected["data"]["id"])
                self.assertEqual(resp.json()["data"]["leave_amount"], expected["data"]["leave_amount"])
                withdraw_after_money = db.select_one_data(case["check_sql"])["leave_amount"]
                logger.info("提现后的用户余额：{}".format(withdraw_after_money))
                self.assertEqual("{:.2f}".format(expected["data"]["leave_amount"]),"{:.2f}".format(float(withdraw_after_money)))

        except AssertionError as e:
            logger.exception("断言失败!")
            raise e





