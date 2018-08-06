import allure,pytest
from Data.input_yml import get_data
from Base.get_driver import get_driver
from time import sleep
from Page.return_page import return_page


class Login_page:
    # def __init__(self):
    #    self.driver = return_page(get_driver())



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
        # 输入账号、密码
        self.send_keys_accpounts_password()
        # 点击登录按钮
        self.click_register_confirm()
        sleep(4)
        # 点击我的按钮
        self.click_my_button()
        sleep(2)
        # 断言
        self.try_except_dim('我的订单')
        self.try_except_dim('首页')
        self.try_except_dim_phone('1319869****')

    """登录功能的正确性验证"""
    @allure.step(title='登录功能的正确性验证')
    @pytest.mark.parametrize('case_name,loc_accounts,loc_password,accounts,password,category_1,category_2,get_news,try_accounts,tag', get_data())
    def test_register(self,case_name,loc_accounts,loc_password,accounts,password,category_1,category_2,get_news,try_accounts,tag):
        allure.attach("用例编号", "{}".format(case_name))
        # 屏幕向右滑动三次
        for i in range(3):
            self.driver.right_downward_slide()
        # 点击进入爱优品按钮
        self.click_access_love_youpin()
        # 点击始终允许按钮
        self.click_allow_button()
        # 点击我的按钮
        self.click_my_button()
        # 点击马上登录按钮
        self.send_keys_accpounts_password_1(loc_accounts,loc_password,accounts,password,category_1,category_2)
        # 点击登录按钮
        self.click_register_confirm()
        sleep(2)
        # 断言
        if tag:
            try:
                # 获取toast
                toast = self.return_register_page().get_toast(get_news)
                # 判断账户是否在页面
                self.try_except_dim_phone(try_accounts)
                # 上划屏幕
                self.up_slide()
                # 点击退出当前账号
                self.click_quit_accounts()
                # 点击确定按钮
                self.click_confirm_quit()
                # 下滑屏幕
                self.below_slide()
                # 断言
                assert toast == try_accounts
            except Exception as E:
                # 截图
                self.screenshot()
                # 返回登录页面
                self.return_register_page()
                assert False
        else:
            try:
                # 获取toast
                toast = self.return_register_page().get_toast(get_news)
                if toast:
                    assert toast == try_accounts
                else:
                    assert False
            finally:
                self.return_register_page()




