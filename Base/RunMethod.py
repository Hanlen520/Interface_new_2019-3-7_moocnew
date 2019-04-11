import requests


class RunMethod:
    def post_main(self,url,data=None,header=None):
        print(url,data,header)

        if header !=None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        print('请求结果',res)

        return res.json()


    def get_main(self,url,data=None,header=None):

        if header !=None:
            res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url,data=data)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        if method=='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res
if __name__ == '__main__':
    r = RunMethod()
    url = "http://211.159.144.66/auth/login"
    #payload = "{\n    \"loginType\": \"1\",\n    \"userIdentification\": \"test1\",\n    \"pwdOrVerifyCode\": \"test\",\n    \"imageVerifyCode\": \"5295\",\n    \"imageVerifyCodeId\": \"7844eba178ea4efe8857a77c1b8946f6\"\n}"
    payload = ''' {
    "loginType": "1",
    "userIdentification": "test1",
    "pwdOrVerifyCode": "test",
    "imageVerifyCode": "5295",
    "imageVerifyCodeId": "7844eba178ea4efe8857a77c1b8946f6"
}'''
    #print("测试数据里的类型==",type(payload))
    header = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "759386d5-3656-4032-bc5a-f04d59f89a73"
    }

    print(r.post_main(url,payload,header))


