"""
    def check_value(jdict, key):
        if isinstance(jdict, list):
            for element in jdict:
                check_value(element, key)
        elif isinstance(jdict, dict):
            if key in list(jdict.keys()):
                if jdict[key]:
                    try:
                        raise FoundException
                    except FoundException as e:

                        value.append(jdict[key])
            else:
                A = []
                B = {}

                for y in list(jdict.keys()):

                    if type(jdict[y]) == type(A):
                        for z in jdict[y]:
                            check_value(z, key)

                    elif type(jdict[y]) == type(B):
                        check_value(jdict[y], key)
        return value

    value = []

    def check_value(jdict, key):
        if isinstance(jdict, list):
            for element in jdict:
                check_value(element, key)
        elif isinstance(jdict, dict):
            if key in list(jdict.keys()):
                if jdict[key]:
                    try:
                        raise FoundException
                    except FoundException as e:

                        value.append(jdict[key])
            else:
                A = []
                B = {}

                for y in list(jdict.keys()):

                    if type(jdict[y]) == type(A):
                        for z in jdict[y]:
                            check_value(z, key)

                    elif type(jdict[y]) == type(B):
                        check_value(jdict[y], key)
        return value


"""



value = []


def check_value(jdict, key):
    if isinstance(jdict, list):
        for element in jdict:
            check_value(element, key)
    elif isinstance(jdict, dict):
        if key in list(jdict.keys()):
            value.append(jdict[key])
        else:
            A = []
            B = {}
            for y in list(jdict.keys()):
                if type(jdict[y]) == type(A):
                    for z in jdict[y]:
                        check_value(z, key)
                elif type(jdict[y]) == type(B):
                    check_value(jdict[y], key)
    return value
d = {
    "code": 0,
    "msg": "success",
    "data": {
        "verifyCodeUrl": "http://zhonghuan-1257386775.cos.ap-beijing.myqcloud.com/chedui-web/2019/03/14/4c8b26df862b4fe6869c9174070d2e31.jpg",
        "verifyCodeId": "5092e3b6c89e45d9bfc052060aa55b2d"
    }
}

import requests
def main_test():
    url = "http://62.234.197.128/basic-data/data/trailer/list"

    payload = "{\n    \"trailerPlateList\":[] ,\n    \"assignCodeList\": [],\n    \"page\": 1,\n    \"pageSize\": 10\n}"
    headers = {
        'Content-Type': "application/json",
        'X-Auth-Token': "39d124367fcf40b3aad5d270c0aeb406",
        'cache-control': "no-cache",
        'Postman-Token': "b93cb8e2-93b6-42ee-ab9b-01ca845d13df"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
#print(check_value(d,'verifyCodeUrl'))
#main_test()
import random
def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)   # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str




# -*- coding: utf-8 -*-
import random
def generate_verification_code(len=6):
    ''' 随机生成6位的验证码 '''
    # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
    # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123): #对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code

import string
def phone_num(num):
    all_phone_nums=[]
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    for i in range(num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits,8))
        res = start+end
        all_phone_nums.append(res)
    return all_phone_nums
    # with open('phone_num.txt','w',encoding='utf-8') as fw:
    #     fw.writelines(all_phone_nums)
phone_num(1000)

#print(generate_verification_code(len=6))
print(phone_num(10))