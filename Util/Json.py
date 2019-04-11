import json
import os
path = os.path.abspath('.')
from Util.common_util import CommonUtil
class OperetionJson:

    def __init__(self):
        self.data = self.read_data()
        self.com_util = CommonUtil()
    """
    读取json文件
    """
    def read_data(self):
        with open((r'D:\pycharm\Interface_new_2019-3-7_mooc\data1\data.json'),'r',encoding='utf-8') as fp:
            res = fp.read()
            data = json.loads(res)
            return data
    """
    根据关键字获取数据
    """
    def get_data(self,id):
        return json.dumps(self.data[id])

    """获取json字符串后替换某个字符串"""
    def data_change(self,id,key):
        res_data = self.get_data(id)
        res_data_dict =eval(res_data)
        value =  self.com_util.check_value(res_data_dict,key)
        return value



if __name__ == '__main__':
    ojson = OperetionJson()
    #print(ojson.get_data('add_gua'))
    ojson.data_change('add_gua',"trailerPlate")


