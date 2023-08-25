from Helper.basePage import BasePage
from Locators.locators import LoginLocators, SignUpLocator
from Logs import logs_file


class Facebook_Login_and_Signup(BasePage):
    log = logs_file.get_logs()

    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context

    def openFaceBookPage(self, URL):
        self.navigate_to_url(URL)

    def getTitleinPage(self):
        return self.get_title()

    def verifyFacebookloginForm(self):
        _xpath_prop = "xpath"
        locator_dict = {LoginLocators.facebookLogo: _xpath_prop, LoginLocators.input_field_email: _xpath_prop,
                        LoginLocators.input_field_password: _xpath_prop, LoginLocators.login_button: _xpath_prop,
                        LoginLocators.forgotPassword_link: _xpath_prop,
                        LoginLocators.createAnAccount_button: _xpath_prop}
        self.verify_elements_located(locator_dict)

    def enterEmail(self, email):
        self.sendKeys(text_value=email, locator_properties=LoginLocators.input_field_email)

    def enterPassword(self, password):
        self.sendKeys(text_value=password, locator_properties=LoginLocators.input_field_password)

    def clickLoginButton(self):
        self.elementClick_if_present(locator_properties=LoginLocators.login_button)

    def verifyLoginErrorAlertPage(self):
        _xpath_prop = "xpath"
        locator_dict = {LoginLocators.login_alert_error_box: _xpath_prop,
                        LoginLocators.login_alert_error_box_message: _xpath_prop,
                        LoginLocators.login_alert_error_box_message2: _xpath_prop}

        self.verify_elements_located(locator_dict)

    def clickforgotPasswordLink(self):
        self.elementClick_if_present(locator_properties=LoginLocators.forgotPassword_link)

    def verifyEmailInputBoxPresent(self):
        self.is_element_present(locator_properties=LoginLocators.input_field_email)

    def clickFacebookSignUpLink(self):
        self.elementClick_if_present(locator_properties=LoginLocators.createAnAccount_button)

    def verifySignupPageHeadingPresent(self):
        self.is_element_present(locator_properties=SignUpLocator.SignupFormHeading)

    def enterSignUpFirstname(self, firstName):
        self.sendKeys(text_value=firstName, locator_properties=SignUpLocator.CreateAccountFirstname)

    def enterSignUpLastname(self, lastName):
        self.sendKeys(text_value=lastName, locator_properties=SignUpLocator.CreateAccountLastname)

    def enterSignUpEmail(self, email):
        self.sendKeys(text_value=email, locator_properties=SignUpLocator.CreateAccountEmail)

    def enterSignUpReEnterEmail(self, email):
        self.sendKeys(text_value=email, locator_properties=SignUpLocator.CreateAccountReEnterEmail)

    def enterSignUpPassword(self, password):
        self.sendKeys(text_value=password, locator_properties=SignUpLocator.CreateAccountPassword)


    def selectDate(self, selectDateValue):
        self.dropdownSelectElement(locator_properties=SignUpLocator.CreateAccountBirthday_Day, selector=selectDateValue)

    def selectMonth(self, selectMonthValue):
        self.dropdownSelectElement(locator_properties=SignUpLocator.CreateAccountBirthday_Month, selector=selectMonthValue)

    def selectYear(self, selectYearValue):
        self.dropdownSelectElement(locator_properties=SignUpLocator.CreateAccountBirthday_Year,selector=selectYearValue)

    def clickFacebookSignUpGenderF(self):
        self.elementClick_if_present(locator_properties=SignUpLocator.CreateAccountGenderF)

    def clickFacebookSignUpButton(self):
        self.elementClick_if_present(locator_properties=SignUpLocator.CreateAccountSignUpButton)