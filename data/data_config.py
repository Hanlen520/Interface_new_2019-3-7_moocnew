
class global_var:
    # case_id
    Id = '0'
    case_name='1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend='6'
    data_depend = '7'
    field_depend ='8'
    data = '9'
    expect ='10'
    result = '11'

    """获取caseid
    """
    def get_id(self):
        return global_var.Id

    """获取case名称"""
    def get_casename(self):
        return global_var.case_name
    """获取url
    """
    def get_url(self):
        return global_var.url

    """获取是否运行"""
    def get_run(self):
        return global_var.run

    """获取请求方式"""
    def get_request_way(self):
        return global_var.request_way

    """获取header"""
    def get_header(self):
        return global_var.header

    """获取依赖id"""
    def get_case_depend(self):
        return global_var.case_depend

    """获取依赖数据"""
    def get_data_depend(self):
        return global_var.data_depend

    """获取依赖数据所属字段"""
    def get_field_depend(self):
        return global_var.field_depend

    """获取请求数据"""
    def get_data(self):
        return global_var.data

    """获取预期结果"""
    def get_expect(self):
        return global_var.expect

    """获取实际结果"""
    def get_result(self):
        return global_var.result

    """获取header值"""
    def get_header_value(self):
        # header = {
        # 'Content-Type': "application/json",
        # 'cache-control': "no-cache",
        # 'Postman-Token': "759386d5-3656-4032-bc5a-f04d59f89a73"
        #
        # }
        header = {
    'Content-Type': "application/json",
    'X-Auth-Token': "39d124367fcf40b3aad5d270c0aeb406",
    'cache-control': "no-cache",
    'Postman-Token': "e1065657-64a4-458c-9a72-4ed0a319c747"
    }
        return header

if __name__ == '__main__':
    gl = global_var()
    # u = gl.get_header_value()
    # print(u)
    print(gl.get_result())