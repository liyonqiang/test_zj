from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    """
    # 公用点击方法
    def base_click(self, loc):
        self.driver.find_element(loc[0], loc[1]).click()

    # 公用输入方法
    def base_input(self, loc, text):
        el = self.driver.find_element(loc[0], loc[1])
        el.clear()
        el.send_keys(text)

    # 发送键的方法
    def send(self, num):
        self.driver.keyevent(num)
    """

    # 封装显示等待方法
    # def find_element(self, loc, timeout=30, poll=0.5):
    #     return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 显示等待找元素方法
    def find_element(self, loc, timeout=30, poll=0.5):

        while True:

            try:
                return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                    lambda x: x.find_element(loc[0], loc[1]))






            except Exception:  # 翻页直到找到元素
                # 滑动前打印所有页面元素
                before_source = self.driver.page_source
                self.driver.swipe(130, 450, 100, 180, 3000)
                # 滑动后再次打印
                after_source = self.driver.page_source

                # 判断如果滑动前后页面元素一样， 说明滑动到底部了， 再找不到， 就终止循环
                if before_source == after_source:
                    print("当前页面没有找到该元素: {}".format(loc))
                    break

    # 点击方法
    def base_click(self, loc):
        self.find_element(loc, timeout=3, poll=0.5).click()

    # 输入方法
    def base_input(self, loc, text):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(text)

    # 发送键的方法
    def send(self, num):
        self.driver.keyevent(num)
