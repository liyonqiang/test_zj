from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NotifySelectPage(BaseAction):
    # 通知按钮
    notify_button = By.XPATH, "//*[contains(@text, '通知')]"

    # 右上角选择框
    option_ele = By.XPATH, "//*[contains(@content-desc, '更多选项')]"

    # 显示全部进程选项
    display_all_ele = By.XPATH, "//*[contains(@text, '显示系统进程')]"

    # def __init__(self, driver):
    #     BaseAction.__init__(self, driver)

    # 通知点击
    def page_click_notify(self):
        self.base_click(self.notify_button)

    # 点击右上角选择
    def page_click_select(self):
        self.base_click(self.option_ele)

    # 点击显示系统进程
    def page_click_display(self):
        self.base_click(self.display_all_ele)

    #  发送键返回方法
    def page_back_key_click(self):
        self.send(4)

    # 定义接收元素元组类型处理， 并返回元素
    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])
