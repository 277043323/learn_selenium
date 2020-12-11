from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    driver = None
    url= ''

    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
            self.driver.refresh()
        else:
            self.driver=driver
        if self.url!="":
            self.driver.get(self.url)

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def swith(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    def wer(self):
        pass

