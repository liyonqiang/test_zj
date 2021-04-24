import os, sys

sys.path.append(os.getcwd())
from base.base_driver import BaseDriver
from page.sysytem_click_page import SystemClickPage


class TestAboutMobile:
    def setup(self):
        self.driver = BaseDriver.get_driver()
        self.systempage = SystemClickPage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_mobile_info(self):
        self.systempage.page_system_click()
