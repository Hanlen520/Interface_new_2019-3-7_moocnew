from Util.Excel import OpenrationExcel
from Base.RunMethod import RunMethod
from data.get_data import GetData
from Util.common_util import CommonUtil
from jsonpath_rw import jsonpath,parse


value = []
class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OpenrationExcel()
        self.data = GetData()
        self.com_util = CommonUtil()

    """通过case_id去获取该case_id的整行数据"""
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    """执行依赖测试,获取结果"""
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_from_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        return res

    """根据依赖的key去获取执行依赖测试case的相应数据,然后返回"""
    def get_data_for_key(self,row):
        depend_data_key = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        # json_exe = parse(depend_data)
        # madle = json_exe.find(response_data)
        # return [math.value for math in madle][0]
        response_data_value = self.com_util.check_value(response_data,depend_data_key)
        return response_data_value[0]

    """判断是否有case依赖"""



if __name__ == '__main__':
    de = DependentData("web_002")
    #print(de.get_case_line_data())
    #print(de.run_dependent())
    #print(de.get_data_for_key(1))
    print(de.get_data_for_key(1))


