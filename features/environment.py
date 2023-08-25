import logging
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Helper.basePage import BasePage
from Helper import driverFactory
from Pages.Facebook_Login_and_Signup_Page import Facebook_Login_and_Signup

def before_all(context):
    browser_type = context.config.userdata.get("browser")
    context.browser_type = browser_type



def before_scenario(context, scenario):
    tag = str(scenario.tags)
    print(tag)

    context.driver = logging.FileHandler.selenium_driver = driverFactory.getWebDriverInstance(context.browser_type)
    s=BasePage(context.driver)
    context.facebook_Login_and_Signup=Facebook_Login_and_Signup(s)
    context.driver.maximize_window()
    context.stepid = 1


def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    context.driver.close()
