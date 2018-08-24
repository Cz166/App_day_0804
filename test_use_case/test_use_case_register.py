import pytest,allure,os,sys
from Base.get_driver import get_driver
from Data.input_yml import get_data
from Page.return_page import return_page
sys.path.append(os.getcwd())

class Test_Login:
    # 初始化App
    def setup_class(self):
        self.Dv = return_page(get_driver())
        # 屏幕向右滑动三次
        for i in range(3):
            self.Dv.return_register_page().right_downward_slide()
        # 点击进入爱优品按钮
        self.Dv.return_register_page().click_access_love_youpin()
        # 点击始终允许按钮
        self.Dv.return_register_page().click_allow_button()
        # 点击我的按钮
        self.Dv.return_register_page().click_my_button()
    # 关闭App
    def teardown_class(self):
        self.Dv.driver.quit()

    @allure.step(title='登录功能的正确性验证')
    @pytest.mark.parametrize('case_name,accounts,password,category_1,category_2,dim,tag,immediately_register',get_data())
    def test_register(self, case_name, accounts, password, category_1, category_2,dim, tag,immediately_register):
        allure.attach("用例编号", "{}".format(case_name))
        # 点击马上登录按钮
        self.Dv.return_register_page().clcik_immediately_register()
        # 输入账号、密码
        self.Dv.return_register_page().send_keys_accpounts_password_1(accounts, password, category_1, category_2)
        # 点击登录按钮
        self.Dv.return_register_page().click_register_confirm()
        # 断言
        if tag:
            try:
                # 断言登录成功的账户是否在页面
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
                assert self.Dv.return_register_page().try_except_dim(immediately_register)
            except Exception as E:
                # 截图
                self.Dv.return_register_page().screenshot()
                # 返回我的页面
                self.Dv.return_register_page().login_close_page()
                # 断言马上登录是否在页面
                self.Dv.return_register_page().try_except_dim(immediately_register)
                assert False
        else:
            try:
                #登录失败，断言快速注册元素是否包含于页面
                self.Dv.return_register_page().try_celerity_register()
                # 截图操作
                self.Dv.return_register_page().screenshot()
            finally:
                # 返回我的页面
                self.Dv.return_register_page().login_close_page()
                # 断言页面是否包含马上登录
                self.Dv.return_register_page().try_except_dim(immediately_register)

