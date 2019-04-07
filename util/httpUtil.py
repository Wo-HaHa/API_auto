import requests
import json
from Common.CommonData import commonData
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def post(self,path,data):
        proxies=commonData.proxies
        host=commonData.host
        data_json=json.dumps(data)
        if commonData.token is not None:
            self.headers['token']=commonData.token

        resp_login=self.http.post(url=host+path,proxies=proxies,data=data_json,headers=self.headers)
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)

        return resp_dict

        #
        # asp_dict=json.loads(asp.text)
        # token=asp_dict['object']['token']
        # header['token']=token
        # print(header)
        #
        #
        # resp=http.post("http://192.168.1.203:8083/sys/getUserInfo",proxies=proxies,data=token,headers=header)
        # # print(resp.text)
        # print(resp.status_code)
        # print(resp.text)
        # print(resp.headers)