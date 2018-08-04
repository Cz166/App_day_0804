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

    @allure.step(title='获取text')
    def gain_single_text(self, loc):
        allure.attach('描述', '{}'.format('获取的text为：%s' % self.find_element(loc)))
        return self.find_element(loc).text
    @allure.step(title='获取列表中的text')
    def gain_a_group_text(self,loc):
        allure.attach('描述','{}'.format('获取的列表为：%s'% self.find_elements(loc).text))
        for element in self.find_elements(loc):
            return element.text


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
        allure.attach('获取的列表', '{}'.format(self.gain_a_group_text(Page.my_list)))
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


    """登录操作"""

    @allure.step(title='输入正确帐号、密码，成功登录')
    def succeed_sell(self):
        # 屏幕向右滑动三次
        for i in range(3):
            self.right_downward_slide()
        # 点击进入爱优品按钮
        self.click_access_love_youpin()
        # 点击始终允许按钮
        self.click_allow_button()
        # 点击我要卖按钮
        self.click_I_sell()
        # 输入帐号
        self.send_keys_text(Page.register_acctount, '13198690728')
        allure.attach('输入账户', '{}'.format('13198690728'))
        # 输入密码
        self.send_keys_text(Page.register_passwod, 'aaa123456')
        allure.attach('输入密码', '{}'.format('aaa123456'))
        # 点击登录按钮
        self.click_register_confirm()
        # 点击我的按钮
        self.click_element(Page.my_button)
        # 断言
        self.try_except('1319869')







