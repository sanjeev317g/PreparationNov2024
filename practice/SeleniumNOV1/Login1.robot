*** Settings ***
Library    SeleniumLibrary    
...    run_on_failure=Capture Page Screenshot
...    implicit_wait=0.5s
...    timeout=10s
...    screenshot_root_directory=SeleniumNOV1
Library    Custom.py




*** Variables ***

${login_Button}    //button[.='Login']

*** Test Cases ***
Open a WebLink
    Open Browser    https://practice.expandtesting.com/login    chrome
    Scroll Element Into View    ${login_Button}
    Maximize Browser Window
    Input username    //input[@id='username']    practice
    Input Text    //input[@id='password']    SuperSecretPassword!
    Set Browser Implicit Wait    2s
    Click Button    ${login_Button}
    ${add}=    Addition
    Log    ${add}

Data Driven Test1
    Open Browser    https://practice.expandtesting.com/login    chrome
    Scroll Element Into View    ${login_Button}
    Maximize Browser Window
   
Data Driven Test2
    [Template]    Test with multiple username password
    Username    Password
    fkldfkldsjfkl    kfjdsklfj;dkslfjdls
    lsdjfkldsjfkld;sjf    sdjflkdsjflksd
    dlfjkdsjflk;dsajf    kldfkdlsjfklds;jf
    ljsflkdjsklfjdslkf    lds;jflkdsjflk;sdjflkdsjflksd
    jslkfjdslkfj    lkjfkldsjfkldjsf


    

*** Keywords ***
Input username
    [Arguments]    ${element}    ${username}
    Input Text    ${element}    ${username}

Test with multiple username password
    [Arguments]    ${Username}    ${Password}
    Input Text    //input[@id='username']    ${Username}
    Input Text    //input[@id='password']   ${Password} 
    

