# import pytest
#
# @pytest.fixture()
# def myfixture():
#     print("这是我的初始化操作")
# @pytest.mark.usefixtures("myfixture")#调用myfixture
# def test_first():
#     print("我的第一个测试用例")
#     assert 1==2
# def test_second():
#     print("我的第二个测试用例")
#     assert 1==3
#
# def test_third():
#     print("我的第三个测试用例")
#     assert "a" in "ab"
# def test_fourth():
#     print("我的第四个测试用例")
#     b=[1,2,3]
#     assert "a" in b
#
# def test_five():
#    assert assValue(3,5)
# def assValue(a,b):
#     if a>b:
#         return False
#     if a<b:
#         return True
#
#
#
#
# if __name__ == '__main__':
#     pytest.main("-s")
