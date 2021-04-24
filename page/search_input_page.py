from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SearchInputPage(BaseAction):
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"

    # 输入文本框
    input_text_button = By.ID, "android:id/search_src_text"

    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # def __init__(self, driver):
    #     BaseAction.__init__(self, driver)

    # 点击搜索
    def page_click_search_button(self):
        self.base_click(self.search_button)

    # 输入文本按钮
    def page_input_text(self, text):
        self.base_input(self.input_text_button, text)

    # 点击返回按钮
    def page_click_back_button(self):
        self.base_click(self.back_button)

    # 定义接收元素元组类型处理， 并返回找到元素
    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])