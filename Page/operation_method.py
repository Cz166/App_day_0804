import time,Page,allure
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Data.input_yml import get_data
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from Base.Base import Base

class method(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)


    """
    获取text属性值
    """
    # 获取text
    def gain_single_text(self, loc):
        return self.find_element(loc).text

    # 获取列表
    def gain_a_group_text(self):
        sleep(3)
        return [i.text for i in self.find_elements(Page.my_list)]

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
       allure.attach('图片名字','{}'.format('register_001_%s.png' % now))
       return self.driver.get_screenshot_as_file\
           ('E:/PyCharm 2017.3.4/App_08_04/Screenshot/register_001_%s.png' % now)

    @allure.step(title='断言是否登录成功')
    def try_except_dim_phone(self,dim_phone):
        try:
            assert dim_phone in self.gain_a_group_text()
            allure.attach("状态", "找到")
            return True
        except:
            allure.attach("状态", "未找到")
            return True
        finally:
            self.screenshot()
            allure.attach('页面元素_(text_list)', '{}'.format(self.gain_a_group_text()))

    @allure.step(title='断言页面是否成功跳转')
    def try_except_dim(self,dim):
        try:
            assert dim in self.gain_a_group_text()
            allure.attach("状态", "找到")
            return True
        except:
            allure.attach("状态", "未找到")
            return False
        finally:
            self.screenshot()
            allure.attach('页面元素_(text_list)', '{}'.format(self.gain_a_group_text()))

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
    @allure.step(title='点击退出当前账号按钮')
    def click_quit_accounts(self):
        self.click_element(Page.quit_accounts)
    @allure.step(title='点击确定按钮')
    def click_confirm_quit(self):
        self.click_element(Page.confirm_quit)

    """我的页面"""
    @allure.step(title='点击马上登录')
    def clcik_immediately_register(self):
        self.click_element(Page.immediately_register)
    @allure.step(title='点击返回按钮')
    def click_return_button(self):
        self.click_element(Page.return_button)

    @allure.step(title='输入账号、输入密码')
    def send_keys_accpounts_password(self):
        list = [[Page.register_acctount,'13198690728','输入账号'],[Page.register_passwod,'aaa123456','输入密码']]
        # 输入账号
        for i in list:
            self.send_keys_text(i[0],i[1],i[2])

    @allure.step(title='输入账号、输入密码')
    def send_keys_accpounts_password_1(self,accounts,password,category_1,category_2):
        # 输入账号
        self.send_keys_text(Page.register_acctount,accounts,category_1)
        # 输入密码
        self.send_keys_text(Page.register_passwod,password,category_2)


    def get_toast_news(self, message):
        # 获取提示消息
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.find_element((By.XPATH,xpath), timeout=5, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False


    def login_close_page(self):
        try:
            # 关闭登陆信息输入页
            self.click_return_button()
            allure.attach("关闭状态:", "成功")
        except Exception as e:
            allure.attach("关闭状态:", "失败")
            allure.attach("关闭失败原因:", "%s" % e)









