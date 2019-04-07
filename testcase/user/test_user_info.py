from conftest import http
import pytest
import random
from Common.CommonData import commonData
class Test_load_user_info:
    def test_user_info(self):
        nickName=str(random.randint(10000000,100000000))
        userName='157'+nickName
        register_data={"nickName":nickName,
            "userName": userName,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "",
            "regionId": 1,
            "regionLevel": 1
            }
        register_resp=http.post("/user/saveOrUpdateUser",register_data)
        # print(register_resp)57
        #登录
        login_data = {"userName": userName,
                "password":commonData.password
        }
        login_resp=http.post("/sys/login", login_data)
        # assert login_resp["object"]["userId"]==490
        login_id=login_resp["object"]["userId"]

        #查看用户信息

        user_info_data={"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}
        info_resp = http.post("/user/loadUserList", user_info_data)
        user_info_id=info_resp["object"]["list"][0]["id"]
        user_info_nickName=info_resp["object"]["list"][0]["nickName"]
        assert login_id==user_info_id
        assert user_info_nickName==nickName










