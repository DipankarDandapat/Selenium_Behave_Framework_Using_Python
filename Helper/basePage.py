from selenium.webdriver.support.wait import WebDriverWait

from Helper.seleniumHelper import SeleniumHelper


class BasePage(SeleniumHelper):
    def __init__(self, driver):
        # super(BasePage, self).__init__(driver)
        SeleniumHelper.__init__(self,driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.implicit_wait = 25




