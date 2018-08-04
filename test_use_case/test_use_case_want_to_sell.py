import allure
import pytest
from Page.operation_method import method
from Base.get_driver import get_driver


class Test_Login:
    def setup_class(self):
        self.Dv = method(get_driver())
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @allure.step(title='测试用例_001_无前置条件_初始化App_点击我要卖_正确帐号登录')
    def test_I_sell_register(self):
        self.Dv.succeed_sell()


if __name__ == '__main__':
    pytest.main('test_use_case_want_to_sell.py')