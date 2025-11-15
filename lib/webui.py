import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
MYSTORE = {}

def open_browser():
    wd = webdriver.Chrome()
    MYSTORE['wd'] = wd
    sleep(0.1)


def open_address_page():
    wd = MYSTORE['wd']
    wd.get("http://localhost/mgr/sign.html#")
    sleep(0.1)
    MYSTORE['wd'] = wd

def try_login(username, password):
    wd = MYSTORE['wd']
    if username is not None:
        wd.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
    if password is not None:
        wd.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    wd.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(0.1)

    alert_text = wd.switch_to.alert.text
    print("Alert text is:", alert_text)
    MYSTORE['wd'] = wd
    return alert_text


def success_login():
    wd = MYSTORE['wd']
    user_field = wd.find_element(By.CSS_SELECTOR, "#username") 
    pass_field = wd.find_element(By.CSS_SELECTOR, "#password")  
    login_button = wd.find_element(By.CSS_SELECTOR, "button[][type='submit']") 

    user_field.clear()
    user_field.send_keys('byhy')
    pass_field.clear()
    pass_field.send_keys('88888888')
    login_button.click()
    sleep(0.1)