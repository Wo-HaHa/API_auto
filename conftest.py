import pytest
import json
from util.httpUtil import HttpUtil
from Common.CommonData import commonData


http=HttpUtil()
@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    path="/sys/login"
    data={"userName":commonData.mobile,"password":commonData.password}
    resp_login=http.post(path,data)
    commonData.token = resp_login['object']['token']
    # assert resp_login['code'] == 200
    # print("登录成功")
#
#     # yield
#
#     # resp =http.post("http://192.168.1.203:8083/sys/logout", proxies=proxies, data=data_json, headers=header)
#     # # print(resp.text)
#     # print(resp.status_code)
#     # print(resp.text)
#     # print(resp.headers)
#     # assert resp.status_code==200
#     #
#     # print("退出成功")
