import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver
    # 定位单个元素
    def find_element(self, loc, timeout=15, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    # 定位一组元素
    def find_elements(self, loc, timeout=15, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))
    # 点击元素
    @allure.step(title='点击操作')
    def click_element(self, loc):
        self.find_element(loc).click()
    # 清空输入框且输入内容
    @allure.step(title='输入操作')
    def send_keys_text(self, loc, text, category):
        input_box = self.find_element(loc)
        input_box.clear()
        input_box.send_keys(text)
        allure.attach(category, '{}'.format(text))

    # 获取toast消息
    @allure.step(title='获取toast消息并断言')
    def try_find_toast(self,get_news,timeout=15,poll=0.1):
        try:
            WebDriverWait(self.driver,timeout,poll).until(expected_conditions.presence_of_element_located
                                                               ((By.PARTIAL_LINK_TEXT, get_news)))
            allure.attach('结果','找到')
            print('///////////////////////////')
            return True
        except:
            allure.attach('结果', '未找到')
            print('-------------------------------')
            return False




