import time

from behave import *

from Logs import logs_file
from TestData import test_data
log = logs_file.get_logs()

# Python Behave Step Definition
@given('the user is on the Facebook login page')
def step_impl(context):
    # Code to navigate to the Facebook login page
    context.facebook_Login_and_Signup.openFaceBookPage(test_data.facebook_url)


@then('the user should see the login form')
def step_impl(context):
    # Code to verify the presence of the login form
    context.facebook_Login_and_Signup.verifyFacebookloginForm()
    title = context.facebook_Login_and_Signup.getTitleinPage()
    context.facebook_Login_and_Signup.verifyTextMatch(actualText=title, expectedText="Facebook – log in or sign up")


# Python Behave Step Definition
@when('the user enters valid email"{email_id}" and password "{password}"')
def step_impl(context, email_id, password):
    # Code to enter valid email and password
    context.facebook_Login_and_Signup.enterEmail(email_id)
    context.facebook_Login_and_Signup.enterPassword(password)


@step('the user clicks the "Log In" button')
def step_impl(context):
    # Code to click the "Log In" button
    context.facebook_Login_and_Signup.clickLoginButton()


@then('the user should be logged in successfully')
def step_impl(context):
    # Code to verify successful login
    time.sleep(5)
    title = context.facebook_Login_and_Signup.getTitleinPage()
    log.info(title)
    context.facebook_Login_and_Signup.verifyTextMatch(actualText=title, expectedText="Facebook")




# Python Behave Step Definition
@when('the user enters invalid email"{email_id}" and password "{password}"')
def step_impl(context,email_id,password):
    # Code to enter invalid email and password
    context.facebook_Login_and_Signup.enterEmail(email_id)
    context.facebook_Login_and_Signup.enterPassword(password)



@then('the user should see an error message')
def step_impl(context):
    # Code to verify the presence of an error message
    context.facebook_Login_and_Signup.verifyLoginErrorAlertPage()


# Python Behave Step Definition
@when('the user clicks the "Forgot Password?" link')
def step_impl(context):
    # Code to click on the "Forgot Password?" link
    context.facebook_Login_and_Signup.clickforgotPasswordLink()


@then('the user should be directed to the password reset page')
def step_impl(context):
    # Code to verify the navigation to the password reset page
    context.facebook_Login_and_Signup.verifyEmailInputBoxPresent()
    title = context.facebook_Login_and_Signup.getTitleinPage()
    log.info(title)
    context.facebook_Login_and_Signup.verifyTextMatch(actualText=title, expectedText="Forgotten Password | Can't Log In | Facebook")


# Python Behave Step Definition
@when('the user clicks the "Sign Up" link')
def step_impl(context):
    # Code to click on the "Sign Up" link
    context.facebook_Login_and_Signup.clickFacebookSignUpLink()


@then('the user should be directed to the signup page')
def step_impl(context):
    # Code to verify the navigation to the signup page
    context.facebook_Login_and_Signup.verifySignupPageHeadingPresent()

# Python Behave Step Definition
@given('the user is on the Facebook signup page')
def step_impl(context):
    # Code to verify the navigation to the signup page
    context.facebook_Login_and_Signup.openFaceBookPage(test_data.facebook_url)
    context.facebook_Login_and_Signup.clickFacebookSignUpLink()
    time.sleep(6)


@when('the user enters valid first name, last name, email, password, and birthdate')
def step_impl(context):
    # Code to enter valid signup information
    context.facebook_Login_and_Signup.enterSignUpFirstname("dip")
    context.facebook_Login_and_Signup.enterSignUpLastname("dghhhh")
    context.facebook_Login_and_Signup.enterSignUpEmail("d@gmail.com")
    context.facebook_Login_and_Signup.enterSignUpReEnterEmail("d@gmail.com")
    context.facebook_Login_and_Signup.enterSignUpPassword("d@thhu")
    time.sleep(5)
    context.facebook_Login_and_Signup.selectDate("29")
    context.facebook_Login_and_Signup.selectMonth("4")
    context.facebook_Login_and_Signup.selectYear("1994")
    context.facebook_Login_and_Signup.clickFacebookSignUpGenderF()
    time.sleep(8)


@step('the user clicks the "Sign Up" button')
def step_impl(context):
    # Code to click the "Sign Up" button
    context.facebook_Login_and_Signup.clickFacebookSignUpButton()


@then('the user should see a verification step')
def step_impl(context):
    # Code to verify the presence of a verification step
    pass


# Python Behave Step Definition
@when('the user leaves the first name and last name fields empty')
def step_impl(context):
    # Code to leave required fields empty
    pass


@then('the user should see error messages for the required fields')
def step_impl(context):
    # Code to verify error messages for required fields
    pass


# Python Behave Step Definition
@when('the user enters an invalid email format')
def step_impl(context):
    # Code to enter an invalid email format
    pass


@then('the user should see an error message for the email field')
def step_impl(context):
    # Code to verify the presence of an error message for the email field
    pass


# Python Behave Step Definition
@when('the user enters a weak password')
def step_impl(context):
    # Code to enter a weak password
    pass


@then('the user should see an error message for the password field')
def step_impl(context):
    # Code to verify the presence of an error message for the password field
    pass


# Python Behave Step Definition
@when('the user enters a birthdate indicating they are underage')
def step_impl(context):
    # Code to enter a birthdate indicating underage
    pass


@then('the user should see an error message regarding age eligibility')
def step_impl(context):
    # Code to verify the presence of an error message regarding age eligibility
    pass


# Python Behave Step Definition
@when('the user enters an email that is already registered')
def step_impl(context):
    # Code to enter an existing email
    pass


@then('the user should see an error message indicating the email is already in use')
def step_impl(context):
    # Code to verify the presence of an error message for existing email
    pass


# Python Behave Step Definition
@when('the user fills out the signup form with valid information')
def step_impl(context):
    # Code to check the terms and conditions checkbox
    pass


@step('the user checks the "I agree to the terms and conditions" checkbox')
def step_impl(context):
    pass


@step('the user clicks the "Sign Up" button')
def step_impl(context):
    pass


@then('the user should receive a confirmation email')
def step_impl(context):
    # Code to verify the receipt of a confirmation email
    pass


# Python Behave Step Definition
@when('the user clicks the "Already have an account? Log In" link')
def step_impl(context):
    # Code to click the "Log In" link on the signup page
    pass


@then('the user should be redirected to the login page')
def step_impl(context):
    # Code to verify the redirection to the login page
    pass


# Python Behave Step Definition
@when('the user clicks the "Learn More" link next to the data usage policy')
def step_impl(context):
    # Code to click the "Learn More" link for data usage policy
    pass


@then('the user should be directed to the data usage policy page')
def step_impl(context):
    # Code to verify the navigation to the data usage policy page
    pass
