from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page.operation_method import method
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Lenovo Z90-7'
desired_caps['appPackage'] = 'com.huashidai.cl.lovegoods.lovegoods'
desired_caps['appActivity'] = '.activity.home.PageActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
for i in range(3):
    TouchAction(driver).press(x=965, y=1666).move_to(x=77, y=1582).release().perform()
sleep(2)
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/ip_ll_enter').click()
sleep(5)
driver.find_element(By.ID,'com.android.packageinstaller:id/permission_allow_button').click()
sleep(2)
# 点击我的按钮
# driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my').click()
# 点击我要卖按钮
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_ll_sell').click()
# 输入账号、密码
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_user').send_keys('13198690728')
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_pwd').send_keys('aaa123456')
# 点击登录按钮
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_ll_login').click()
# driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my').click()
def ss(timeout=10,poll=0.01):
    xpath = "//*[contains(@text,'{}')]".format('成功')
    ss = WebDriverWait(driver,timeout,poll).until(expected_conditions.presence_of_element_located
                                                                   ((By.PARTIAL_LINK_TEXT, '成功')))
    return ss.text

el = [i.text for i in driver.find_elements(By.CLASS_NAME,'android.widget.TextView')]
def s():
    try:
        assert ss() == '登录成功'
        print('111111111111111111')
    except:
        print(6666666)
        return False




    # try:
    #     assert '1319869****'in el
    #     print(el)
    #     return True
    # except:
    #     print(00000000000000)
    #     return False
s()
