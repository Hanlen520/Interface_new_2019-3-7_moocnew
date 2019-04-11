import json
import os
import operator

value = []
class CommonUtil:

    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        '''
        str_one = str_one.replace(" ",'')
        if isinstance(str_one,dict) or isinstance(str_two,dict):
            str_two = json.dumps(str_two)
            str_two = str_two.replace(" ",'')
            str_two = str_two.replace("{",'')
            str_two = str_two.replace("}",'')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        print('str1===',str_one)
        print('str2===',str_two)
        print("比较的结果是===",flag)
        return flag

    def find_report_file():
        '''查找目录下最新的文件'''
        adb_path = os.path.abspath('.')
        file_lists = os.listdir(adb_path + "\\" + "report")
        file = os.path.join(adb_path + "\\" + "report", file_lists[len(file_lists) - 1])
        return file

    "判断两个字典是否相等"
    def is_equal_dict(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one,dict_two)

    """遍历解析json数据,根据json字符串与key拿到相应的value"""

    def check_value(self, jdict, key):
        if isinstance(jdict, list):
            for element in jdict:
                self.check_value(element, key)
        elif isinstance(jdict, dict):
            if key in list(jdict.keys()):
                value.append(jdict[key])
            else:
                A = []
                B = {}
                for y in list(jdict.keys()):
                    if type(jdict[y]) == type(A):
                        for z in jdict[y]:
                            self.check_value(z, key)
                    elif type(jdict[y]) == type(B):
                        self.check_value(jdict[y], key)
        return value

    """随机生成字符串"""
    """
    import random

def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

salt = ranstr(6)
print salt
    """



if __name__ == '__main__':
    c = CommonUtil()
    str_one =  '"msg": "success"'
    #s1 = json.dumps(str_one)
    str_two =  '"code": 0, "msg": "success", "data": {"verifyCodeUrl": "http://zhonghuan-1257386775.cos.ap-beijing.myqcloud.com/chedui-web/2019/03/18/a11a44dfefe74303b37c8ae680d86f03.jpg", "verifyCodeId": "6d9124e23fa048b4a98f65d65ef9a773"}'
    #s2 = json.dumps(str_two)
    #print(c.is_contain(str_one,str_two))
    jdict = {"trailerPlate": "1111", "agencyCode": "JG01", "length": "1", "axleNum": "2", "size": "1,1,1", "volumeCapacity": "1", "loadCapacity": ""}
    print(type(jdict))
    print(c.check_value(jdict,'trailerPlate'))
