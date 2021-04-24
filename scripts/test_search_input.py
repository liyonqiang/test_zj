
# allure 报告导包
import allure

import pytest


class TestSearchInput:
    def setup(self):
        pass

    def teardown(self):
        pass

    # 1. 添加测试步骤: @allure.step(title="测试步骤001")
    @allure.step(title="测试步骤001")
    def test_login_001(self):
        # 2. 添加步骤描述
        allure.attach("步骤001描述", "此步骤会打印 001")

        print("001")
        assert 1

    # Severity：严重级别(BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL)
    # 3. 添加严重级别  @pytest.allure.severity(Severity)
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤002")
    def test_login_002(self):
        allure.attach("步骤002描述", "此步骤会打印 002")
        print("002")
        assert 0