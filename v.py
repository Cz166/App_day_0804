from time import sleep

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
driver.find_element(By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my').click()
sleep(2)
el = [i.text for i in driver.find_elements(By.CLASS_NAME,'android.widget.TextView')]
try:
    assert '我的订单'in el
    print(el)
except:
    print(6666666)

