from Util.Excel import OpenrationExcel
from Util.Json import OperetionJson
from data.data_config import global_var


class GetData:
    def __init__(self):
        self.opera_excel = OpenrationExcel()
        self.gl = global_var()

    """获取excel行数"""
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    """获取是否执行"""
    def get_is_run(self,row):
        col = self.gl.get_run()
        run_model = self.opera_excel.get_cell_value(row,int(col))
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    """获取是否有header"""
    def is_header(self,row):
        col = self.gl.get_header()
        header = self.opera_excel.get_cell_value(row,int(col))
        if header == 'yes':
            return self.gl.get_header_value()
        else:
            return None

    """判断请求方式"""
    def get_request_method(self,row):
        col = self.gl.get_request_way()
        request_method = self.opera_excel.get_cell_value(row,int(col))
        return request_method

    """取出url"""
    def get_url(self,row):
        col = self.gl.get_url()
        url = self.opera_excel.get_cell_value(row,int(col))
        return url

    """获取请求数据"""
    def get_request_data(self,row):
        col = self.gl.get_data()
        data = self.opera_excel.get_cell_value(row,int(col))
        if data =='':
            return None
        return data

    """获取关键字拿到data数据"""
    def get_data_from_json(self,row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    """获取预期结果"""
    def get_expect_data(self,row):
        col = self.gl.get_expect()
        expect = self.opera_excel.get_cell_value(row,int(col))
        if expect =='':
            return None
        return expect

    """写入数据"""
    def write_result(self,row,value):
        col = int(self.gl.get_result())+1
        print("要被写入的值为===",value)
        self.opera_excel.write_value(row,col,value)

    """获取依赖的caseID"""
    def get_case_dependID(self,row):
        col = int(self.gl.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        return depend_case_id

    """获取依赖数据的key"""
    def get_depend_key(self,row):
        col = int(self.gl.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key =="":
            return None
        else:
            return depend_key

    """判断是否有keys依赖"""
    def is_depend(self,row):
        col = int(self.gl.get_field_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id =="":
            return None
        else:
            return depend_case_id

    """获取数据依赖字段"""
    def get_depend_field(self,row):
        col = int(self.gl.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data =="":
            return None
        else:
            return data



if __name__ == '__main__':
    g = GetData()
    s = g.write_result(2,"PASS")
    #print(s)
    #print(g.get_depend_key(1))
    #print(g.get_depend_key(1))
    # print(g.get_case_dependID(1))