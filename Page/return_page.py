from Page.operation_method import method

class return_page:
    def __init__(self,driver):
        self.driver = driver
    # 返回登录页面对象
    def return_register_page(self):
        return method(self.driver)