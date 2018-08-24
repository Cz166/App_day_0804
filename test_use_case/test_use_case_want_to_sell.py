import allure,pytest
from Base.get_driver import get_driver
from Data.input_yml import get_data
from Page.return_page import return_page


class Test_Login:
    def setup_class(self):
        self.Dv = return_page(get_driver())
        # 屏幕向右滑动三次
        for i in range(3):
            self.Dv.return_register_page().right_downward_slide()
        # 点击进入爱优品按钮
        self.Dv.return_register_page().click_access_love_youpin()
        # 点击始终允许按钮
        self.Dv.return_register_page().click_allow_button()
    def teardown_class(self):
        self.Dv.driver.quit()
    @allure.step(title='测试用例_001_无前置条件_初始化App_点击我要卖_登录功能正确性验证')
    @pytest.mark.parametrize('case_name,accounts,password,category_1,category_2,dim,tag,immediately_register',get_data())
    def test_register(self, case_name, accounts, password, category_1, category_2, dim,tag,immediately_register):
        allure.attach("用例编号", "{}".format(case_name))
        # 点击我要卖按钮
        self.Dv.return_register_page().click_I_sell()
        # 输入账号、密码
        self.Dv.return_register_page().send_keys_accpounts_password_1(accounts, password, category_1, category_2)
        # 点击登录按钮
        self.Dv.return_register_page().click_register_confirm()
        # 断言我的按钮是否存在
        self.Dv.return_register_page().try_my_button()
        # 断言
        if tag:
            try:
                self.Dv.return_register_page().click_register_confirm()
                # 点击我的按钮
                self.Dv.return_register_page().click_my_button()
                # 判断账户是否在页面
                self.Dv.return_register_page().try_except_dim(dim)
                # 上划屏幕
                self.Dv.return_register_page().up_slide()
                # 点击退出当前账号
                self.Dv.return_register_page().click_quit_accounts()
                # 点击确定按钮
                self.Dv.return_register_page().click_confirm_quit()
                # 下滑屏幕
                self.Dv.return_register_page().below_slide()
                # 断言马上登录是否在页面
                self.Dv.return_register_page().try_except_dim(immediately_register)
            except Exception as E:
                # 截图
                self.Dv.return_register_page().screenshot()
                # 返回主页面
                self.Dv.return_register_page().login_close_page()
                # 断言页面是否找到我的按钮
                self.Dv.return_register_page().try_my_button()
        else:
            try:
                # 登录失败，断言快速注册是否包含于页面
                self.Dv.return_register_page().try_celerity_register()
            except Exception as E:
                # 截图操作
                self.Dv.return_register_page().screenshot()
                allure.attach('错误信息','{}'.format(E))
                assert False
            finally:
                # 回到主页面
                self.Dv.return_register_page().login_close_page()
                # 判断是否定位到我的按钮
                self.Dv.return_register_page().try_my_button()