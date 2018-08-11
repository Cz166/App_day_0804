

# def s():
#     list = [2,4,5,7,1]
#     try:
#         assert 2 in list
#         print(True)
#     except:
#         print(False)
#     finally:
#         print('aaaaaaaaa')


# s()

def get_toast_news(get_news):
    # 获取提示消息

    xpath = "//*[contains(@text,'{}')]".format(get_news)
        # toast_message = self.find_element((By.XPATH, xpath), timeout=5, poll=0.1)
        # return toast_message.text
    print(xpath)
get_toast_news('1111')
