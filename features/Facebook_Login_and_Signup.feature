
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


  Scenario: User leaves required fields empty on signup form
    Given the user is on the Facebook signup page
    When the user leaves the first name and last name fields empty
    And the user clicks the "Sign Up" button
    Then the user should see error messages for the required fields


  Scenario: User enters an invalid email format on signup form
    Given the user is on the Facebook signup page
    When the user enters an invalid email format
    And the user clicks the "Sign Up" button
    Then the user should see an error message for the email field


  Scenario: User enters a weak password on signup form
    Given the user is on the Facebook signup page
    When the user enters a weak password
    And the user clicks the "Sign Up" button
    Then the user should see an error message for the password field


  Scenario: User is underage on signup form
    Given the user is on the Facebook signup page
    When the user enters a birthdate indicating they are underage
    And the user clicks the "Sign Up" button
    Then the user should see an error message regarding age eligibility


  Scenario: User tries to use an existing email on signup form
    Given the user is on the Facebook signup page
    When the user enters an email that is already registered
    And the user clicks the "Sign Up" button
    Then the user should see an error message indicating the email is already in use


  Scenario: User agrees to the terms and conditions on signup form
    Given the user is on the Facebook signup page
    When the user fills out the signup form with valid information
    And the user checks the "I agree to the terms and conditions" checkbox
    And the user clicks the "Sign Up" button
    Then the user should receive a confirmation email

  Scenario: User navigates back to login from signup form
    Given the user is on the Facebook signup page
    When the user clicks the "Already have an account? Log In" link
    Then the user should be redirected to the login page



  Scenario: User clicks on "Learn More" for data usage policy on signup form
    Given the user is on the Facebook signup page
    When the user clicks the "Learn More" link next to the data usage policy
    Then the user should be directed to the data usage policy page
