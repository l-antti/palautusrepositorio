*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  validuser
    Set Password  validpassword123
    Set Password Confirmation  validpassword123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  va
    Set Password  validpassword123
    Set Password Confirmation  validpassword123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long


Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  val
    Set Password Confirmation  val
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long
    

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  validpassword
    Set Password Confirmation  validpassword
    Submit Registration
    Registration Should Fail With Message  Password must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  validpassword123
    Set Password Confirmation  differentpassword456
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Create User  existinguser  validpassword123
    Set Username  existinguser
    Set Password  validpassword123
    Set Password Confirmation  validpassword123
    Submit Registration
    Registration Should Fail With Message  Username already taken
    
*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page