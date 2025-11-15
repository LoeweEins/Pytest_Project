import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.webui import open_browser, open_address_page,try_login, success_login, MYSTORE

# pytestmark = pytest.mark.网页测试 # 标记该模块为 网页测试 标签
pytestmark = [pytest.mark.网页测试, pytest.mark.登录测试] # 标记该模块为 多个标签

def setup_module(module):
    open_browser()
def teardown_module(module):
    wd = MYSTORE['wd']
    wd.quit()

@pytest.mark.webtestclass1 # 标记该类为 webtestclass1 标签
@pytest.mark.webtestclass2 # 标记该类为 webtestclass2 标签
class Test_错误登录: # 类名必须以 Test_ 开头

    @classmethod
    def setup_class(cls):
        open_address_page()
####

    def teardown_method(self):
        wd = MYSTORE['wd']
        wd.switch_to.alert.accept()
        sleep(0.1)
        wd.find_element(By.CSS_SELECTOR, "#username").clear()
        wd.find_element(By.CSS_SELECTOR, "#password").clear()
        MYSTORE['wd'] = wd


    @pytest.mark.parametrize("username,password,expected_alert", [
        (None, '88888888', "请输入用户名"),
        ('byhy', None, "请输入密码"),
        ('byhy', 'wrongpassword', "登录失败 : 用户名或者密码错误"),
    ])
    @pytest.mark.webtest # 标记该套件为 webtest 标签
    def test_UI_0001_0003(self, username, password, expected_alert):
        print('\n用例UI_0001_0003')
        
        alert_text = try_login(username, password)
        assert alert_text == expected_alert
        
    


class Test_错误密码: # 类名必须以 Test_ 开头

    def test_C001001(self): # 方法名必须以 test_ 开头        
        pass
    def test_C001002(self):
        pass
    def test_C001003(self):
        pass