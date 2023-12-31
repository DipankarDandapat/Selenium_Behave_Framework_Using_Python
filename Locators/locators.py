class SignUpLocator:
    SignupFormHeading="// div[contains(text(), 'Sign Up')]"
    CreateAccountFirstname = "//input[@name='firstname']"
    CreateAccountLastname = "//input[@name='lastname']"
    CreateAccountEmail = "//input[@name='reg_email__']"
    CreateAccountReEnterEmail = "//input[@name='reg_email_confirmation__']"
    CreateAccountPassword = "//input[@name='reg_passwd__']"
    CreateAccountBirthday_Day = "//select[@name='birthday_day']"
    CreateAccountBirthday_Month = "//select[@name='birthday_month']"
    CreateAccountBirthday_Year = "//select[@name='birthday_year']"
    CreateAccountGenderF = "//label[contains(text(),'Female')]"
    CreateAccountSignUpButton="//button[contains(@name,'websubmit')]"

class LoginLocators:
    facebookLogo="// img[ @ alt = 'Facebook']"
    input_field_email = "//input[@name='email']"
    input_field_password = "//input[@name='pass']"
    login_button = "//button[@name='login']"
    forgotPassword_link = "//a[normalize-space()='Forgotten password?']"
    createAnAccount_button = "//a[contains(text(),'Create new account')]"
    login_alert_error_box = "//div[@id='error_box']"
    login_alert_error_box_message="// div[contains(text(), 'Wrong credentials')]"
    login_alert_error_box_message2="// div[contains(text(), 'Invalid username or password')]"
