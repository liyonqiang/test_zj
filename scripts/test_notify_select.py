import sys, os

sys.path.append(os.getcwd())

from base.base_driver import BaseDriver
from page.notify_select_page import NotifySelectPage


class TestNotifySelect:
    def setup(self):
        # 从base_driver获取driver对象
        self.driver = BaseDriver.get_driver()
        # self.driver.implicitly_wait(30)

        # 获取对应的page页面对象
        self.notifyselectpage = NotifySelectPage(self.driver)

    # 关闭driver对象
    def teardown(self):
        self.driver.quit()

    # 查看显示系统进程
    def test_notify_select(self):
        # 点击通知
        self.notifyselectpage.page_click_notify()
        # 点击右上角选择
        self.notifyselectpage.page_click_select()
        # 点击显示系统进程
        self.driver.find_element_by_xpath("//*[contains(@text, '显示系统进程')]").click()
        # 按下返回键
        self.notifyselectpage.page_back_key_click()
