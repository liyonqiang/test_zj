from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SystemClickPage(BaseAction):
    # 系统按钮
    system_button = By.XPATH, "//*[contains(@text, '关于平板电脑')]"

    # 关于手机信息点击
    def page_system_click(self):
        self.base_click(self.system_button)
