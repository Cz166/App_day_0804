from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
# desired_caps['automationName'] = 'Uiautomator2'
desired_caps['deviceName'] = 'Lenovo Z90-7'
desired_caps['appPackage'] = 'com.ss.android.ugc.live'
desired_caps['appActivity'] = '.main.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# sleep(3)
# for i in range(2):
#     driver.find_element(By.ID,'com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element(By.ID,'com.phonegap.cqmmgo:id/login').click()
# driver.find_element(By.ID,'com.phonegap.cqmmgo:id/phone_login_txt').click()
# driver.find_element(By.ID,'com.phonegap.cqmmgo:id/username_edittext').send_keys('16601035178')
# driver.find_element(By.ID,'com.phonegap.cqmmgo:id/password_edittext').send_keys('Acheng75751244！！')
# driver.find_element(By.ID,'com.phonegap.cqmmgo:id/login_btn').click()


driver.find_element(By.ID,'com.ss.android.ugc.live:id/a7n').click()
driver.find_element(By.ID,'com.phonegap.cqmmgo:id/login').click()
driver.find_element(By.ID,'com.phonegap.cqmmgo:id/phone_login_txt').click()
driver.find_element(By.ID,'com.phonegap.cqmmgo:id/username_edittext').send_keys('16601035178')
driver.find_element(By.ID,'com.phonegap.cqmmgo:id/password_edittext').send_keys('Acheng75751244！！')
driver.find_element(By.ID,'com.phonegap.cqmmgo:id/login_btn').click()

sleep(15)
def try_find_toast(timeout=19,poll=0.1):
    try:
        WebDriverWait(driver,timeout,poll).until(expected_conditions.presence_of_element_located
                                                           ((By.PARTIAL_LINK_TEXT, '成功')))
        print('///////////////////////////')
        return True
    except:
        print('-------------------------------')
        return False


try_find_toast()

driver.quit()