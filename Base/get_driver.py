from appium import webdriver

# 初始化App
def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'Lenovo Z90-7'
    desired_caps['appPackage'] = 'com.huashidai.cl.lovegoods.lovegoods'
    desired_caps['appActivity'] = '.activity.home.PageActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
