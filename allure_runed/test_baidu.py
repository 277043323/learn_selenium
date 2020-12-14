import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature("test")
class Test_Baidu_Search:

    def setup(self):
        with allure.step("准备工作"):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    Test_Case_Link ="https://www.github.com"
    @allure.issue(Test_Case_Link,"用例地址")
    @allure.story("search_test")
    @pytest.mark.parametrize("data",("王者荣耀","今日头条","pytest"))
    def test_baidu_search(self,data):
        with allure.step("获取测试地址"):
            self.driver.get("https://www.baidu.com")
        with allure.step("输入关键字"):
            self.driver.find_element(By.ID,'kw').send_keys(data)
        with allure.step("点击搜索"):
            self.driver.find_element(By.ID,"su").click()
        with allure.step("关闭当前窗口"):
            self.driver.close()
