Feature: Connect pages tests

  Scenario: Users can do password reset
    When Opening the password-reset page
    Given Enter email svetlana@whil.com
    Then Click reset button
    Then Make sure user sees Reset Confirmation

  Scenario: Users can click login on reset page
    When Opening the password-reset page
    Given Enter email svetlana@whil.com
    Then Click reset button
    Then Click login button

  Scenario: Users can complete Coaching Tips
    When Opening the login page
    Given Logging in with svetlana@whil.com and Passw0rd!
    Then Complete Coaching Tips
    Then Make sure user is on the home page
    Then Opening the login page

  Scenario Outline: Users cannot Login with invalid entries
    When Opening the login page
    Given Logging in with <email> and <password>
    Then Make sure user sees login error

    Examples:
    |email        |password |
    |test@test.com|Pass     |
    |test         |Passw0rd!|


  Scenario: Users can Login with valid credentials using ENTER key
    When Opening the login page
    Given Logging in with svetlana@whil.com and Passw0rd!
    Then Skip Coaching Tips
    Then Make sure user is on the home page
    Then Opening the login page

  Scenario: Users can Login with valid credentials clicking on Login bttn
    When Opening the login page
    Given Logging in: svetlana@whil.com and Passw0rd! clicking Login button
    Then Skip Coaching Tips
    Then Make sure user is on the home page
    Then Opening the login page

  Scenario: Users can click through WhilPower categories
    When Opening the login page
    Given Logging in with svetlana@whil.com and Passw0rd! and skipping Coahing Tips
#    Then Click WhilPower button
#    Then Opening the login page
