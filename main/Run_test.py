import os
#os.sys.path.append("D:\pycharm\Interface_new_2019-3-7_mooc")
#os.sys.path.append(os.path.join( os.path.dirname(__file__), '../..'))
os.sys.path.append("..")
from Base.RunMethod import RunMethod
from data.get_data import GetData
from Util.common_util import CommonUtil
from Util.send_email import SendEmail
from data.dependent_data import DependentData
import json


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()

    """程序执行的主入口"""

    def go_on_run(self):
        pass_count = []
        fail_count = []

        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)

                request_data = self.data.get_data_from_json(i)
                expect = self.data.get_expect_data(i)

                header = self.data.is_header(i)
                depend_case_id = self.data.get_case_dependID(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case_id)
                    # 获取依赖相应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data_dict = eval(request_data)
                    request_data_dict[depend_key] = depend_response_data

                res = self.run_method.run_main(method,url,request_data,header)
                print("执行结果为==",res)

                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i+1,"PASS")
                    pass_count.append(i)
                else:
                    #self.data.write_result(i+1,"FAIL")
                    res = json.dumps(res)
                    self.data.write_result(i + 1,res)
                    fail_count.append(i)
        print("通过的结果为===",len(pass_count))
        #self.send_email.send_main(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()








