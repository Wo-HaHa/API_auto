import pytest
import requests
from Common.CommonData import commonData
from conftest import http
class Test_login:
    def test_login_success(self):
        data={
            "userName":commonData.mobile,
            "password":commonData.password
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==200
        assert resp['msg']=="操作成功"
        assert resp["object"]["userId"]==130
        print("登录成功")

    def test_login_fail(self):
        data = {
            "userName": commonData.mobile,
            "password": "123456789"
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == "用户名或密码错误"
        print("登录失败，密码错误")
    def test_login_fail1(self):
        data = {
            "userName": "123456789",
            "password": commonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == "用户不存在"
        print("登录失败，用户不存在")

    def test_login_fail2(self):
        data = {
            "userName": "",
            "password": commonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == "此账户禁止登录"
        print("登录失败，此账户禁止登录")

    def test_login_fail3(self):
        data = {
            "userName": "",
            "password": commonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == "此账户禁止登录"
        print("登录失败，此账户禁止登录")




if __name__ == '__main__':
    pytest.main(['-s'])