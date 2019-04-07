import pytest
import requests
from Common.CommonData import commonData
import allure
from conftest import http
@allure.feature("修改密码成功")
class Test_changepwd:
    @allure.story("修改密码成功")
    @pytest.mark.usefixtures("recoverPwd")
    def test_changepwd(self):
        newpwd="123456789"
        data = {
            "userId": "130",
            "userName": commonData.mobile,
            "oldPwd":"123456",
            "password":newpwd
        }
        resp = http.post('/sys/changePwd', data)
        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
        print("修改密码成功")

    # def test_changepwd1(self):
    #     data = {
    #         "userId": "130",
    #         "userName": commonData.mobile,
    #         "oldPwd":"123456",
    #         "password":"123456789"
    #     }
    #     resp = http.post('/sys/changePwd', data)
    #     assert resp['code'] == 411
    #     assert resp['msg'] == "旧密码错误"
    #     print("修改密码失败，旧密码错误")


    @pytest.fixture()
    def recoverPwd(self):
        newpwd="123456"
        yield
        data={
            "userId": "130",
            "userName": commonData.mobile,
            "oldPwd": "123456789",
            "password": newpwd
        }
        resp = http.post('/sys/changePwd', data)

