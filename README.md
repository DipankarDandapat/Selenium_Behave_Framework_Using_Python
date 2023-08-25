# Python Behave Framework with Selenium
Welcome to the Python Behave Framework! This repository serves as a starting point for using the Behave framework for behavior-driven development (BDD) with Python.

## Getting Started

Follow these steps to set up and start using the Python Behave framework for your project:

## Prerequisites

- Python: Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

## Description

Test Automation Framework using selenium and Python with the below features:

- Framework is based on page object model.
- Reporting using Allure report.
- Upload Allure report ON Google Cloud Storage.
- Send Report via Google Gmail.
- Reading locators from Class file.
- Reading test data from JSON file.
- Generate Log file.
- Re-Run the failed Scenario.
- Run code with Chrome/Firefox/Edge Local Browser.
- Run code with cloud like BrowserStack and LambdaTest

## Install dependences

To install the packages listed in a requirements.txt file for your Python project, you can use the pip package manager. The requirements.txt file typically contains a list of package names along with their version specifications. Here's how you can install the packages using pip:

- Open a terminal or command prompt.

- Navigate to the directory where your requirements.txt file is located. Use the cd command to change directories.

```bash
cd /path/to/your/project
```
- Install the packages using pip and the -r flag followed by the path to your requirements.txt file:

``` bash
pip install -r requirements.txt
```
This command will read the requirements.txt file, download the specified packages, and install them into your project's Python environment.

Make sure you have Python and pip installed and available in your system's PATH before running these commands. If you're using a virtual environment, activate the environment first before running the pip install command.

For example, if you have a requirements.txt file that looks like this:

``` makefile
requests==2.25.1
beautifulsoup4==4.9.3
```
Running pip install -r requirements.txt will install the specified versions or higher versions of the listed packages.

Remember to keep your requirements.txt file up-to-date as you add or remove dependencies for your project. You can use the following command to generate an updated requirements.txt file based on your current environment:

```bash
pip freeze > requirements.txt
```
This command will overwrite the existing requirements.txt file with the currently installed package versions.




## Writing Feature Files
Behave tests are written using Gherkin syntax in feature files. Create a features directory in your project and add .feature files inside it. For example, my_feature.feature:
```bash
Feature: Facebook Login and Signup
  # Enter feature description here
 @logincase
  Scenario: User navigates to the Facebook login page
    Given the user is on the Facebook login page
    Then the user should see the login form

  @logincase
  Scenario Outline: User enters valid login credentials
    Given the user is on the Facebook login page
    When the user enters valid email"<email_id>" and password "<password>"
    And the user clicks the "Log In" button
    Then the user should be logged in successfully
    Examples: Credentials
      | email_id | password |
      |dipak@gmail.com|Dipak|
    
@logincase
 Scenario Outline: User enters invalid login credentials
    Given the user is on the Facebook login page
    When the user enters invalid email"<email_id>" and password "<password>"
    And the user clicks the "Log In" button
    Then the user should see an error message
   Examples:
     | email_id | password |
     |dipak@gmail.com|Dipak|
  
  Scenario: User clicks on "Forgot Password?" link
    Given the user is on the Facebook login page
    When the user clicks the "Forgot Password?" link
    Then the user should be directed to the password reset page
    
@signupcase
  Scenario: User navigates to the Facebook signup page
    Given the user is on the Facebook login page
    When the user clicks the "Sign Up" link
    Then the user should be directed to the signup page
  
@signupcase
  Scenario: User fills out the signup form with valid information
    Given the user is on the Facebook signup page
    When the user enters valid first name, last name, email, password, and birthdate
    And the user clicks the "Sign Up" button
    Then the user should see a verification step
```


## Writing Step Definitions

Step definitions are Python code that map the steps in your feature files to actual code that performs the actions. Create a directory named features/steps and add a Python file, e.g., my_steps.py:

```bash
from behave import given, when, then

@given('the user is on the Facebook login page')
def step_impl(context):
    # Code to navigate to the Facebook login page
    pass

@when('the user enters valid email"{email_id}" and password "{password}"')
def step_impl(context, email_id, password):
    # Code to enter valid email and password
    pass

@step('the user clicks the "Log In" button')
def step_impl(context):
    # Code to click the "Log In" button
   pass

@then('the user should be logged in successfully')
def step_impl(context):
    # Code to verify successful login
    pass

```
# Running Tests
To run your Behave tests, navigate to the root of your project and run the following command:
```bash
behave
```

# Further Resources

- [Behave Documentation](https://behave.readthedocs.io/en/latest/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)

# License
This project is licensed under the MIT License.
```bash

Just copy the above markdown content, paste it into a file named `README.md`, and save it in your project directory. This will give you a basic README.md file for your Python Behave framework project. Remember to customize it with your specific project details and any additional information you'd like to include.

```
