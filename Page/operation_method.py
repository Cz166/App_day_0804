import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Page
from Base.Base import Base
import allure

class method(Base):
    def __init__(self,driver):
       Base.__init__(self,driver)


    """
    获取toast消息
    """
    @allure.step(title='获取toast消息')
    def get_toast(self,message):
        xpath = '//*[contains(@text,"{}")]'.format(message)
        return self.find_element(By.XPATH,xpath).text


    """
    获取text属性值
    """

    def gain_single_text(self, loc):
        return self.find_element(loc).text
    def gain_a_group_text(self,loc):
        text_list = []
        for element in self.find_elements(loc):
            text_list.append(element.text)
            return text_list


    """屏幕滑动"""

    @allure.step(title='向右滑动')
    def right_downward_slide(self):
        TouchAction(self.driver).press(x=965, y=1666).move_to(x=77, y=1582).release().perform()
    @allure.step(title='向上滑动')
    def up_slide(self):
        TouchAction(self.driver).press(x=481, y=1672).move_to(x=504, y=691).release().perform()
    @allure.step(title='向下滑动')
    def below_slide(self):
        TouchAction(self.driver).press(x=504, y=691).move_to(x=481, y=1672).release().perform()

    """截图操作"""
    @allure.step(title='截图操作')
    def screenshot(self):
       now =  time.strftime('%Y-%m-%d_%H_%M_%S')
       allure.attach('描述','{}'.format('图片的名字是：register_001_%s.png' % now))
       return self.driver.get_screenshot_as_file\
           ('E:/PyCharm 2017.3.4/App_08_04/Screenshot/register_001_%s.png' % now)

    @allure.step(title='断言是否登录成功')
    def try_except(self,dim_phone):
        allure.attach('获取登录成功的账号', '{}'.format(self.gain_a_group_text(Page.my_list)))
        try:
            dim_phone in self.gain_a_group_text(Page.my_list)
        except:
            assert False
        finally:
            self.screenshot()


    """初始页面"""
    @allure.step(title='点击启动页面_教程_进入爱优品按钮')
    def click_access_love_youpin(self):
        self.click_element(Page.access_love_youpin)
    @allure.step(title='点击始终允许')
    def click_allow_button(self):
        self.click_element(Page.allow_button)


    """我要卖页面"""
    @allure.step(title='点击我要卖按钮')
    def click_I_sell(self):
        self.click_element(Page.I_want_to_sell)
    @allure.step(title='点击登录按钮')
    def click_register_confirm(self):
        self.click_element(Page.register_confirm)
    @allure.step(title='点击我的按钮')
    def click_my_button(self):
        self.click_element(Page.my_button)

    @allure.step(title='输入账号、输入密码')
    def send_keys_accpounts_password(self):
        list = [['Page.register_acctount','输入账号','13198690728'],['Page.register_passwod','输入密码','aaa123456']]
        # 输入账号
        for i in list:
            self.send_keys_text(i[0],i[1],i[2])


    """登录操作"""

    @allure.step(title='输入正确帐号、密码，成功登录')
    def succeed_sell(self):
        # 屏幕向右滑动三次
        for i in range(3):
            self.right_downward_slide(),i
        # 点击进入爱优品按钮
        self.click_access_love_youpin()
        # 点击始终允许按钮
        self.click_allow_button()
        # 点击我要卖按钮
        self.click_I_sell()
        # 输入账号、密码
        self.send_keys_accpounts_password()
        # 点击登录按钮
        self.click_register_confirm()
        # 点击我的按钮
        self.click_my_button()
        # 断言
        self.try_except('1319869')







