*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}    https://www.amazon.in/
${URL1}    https://www.google.com/
${USERNAME}    myUserName
${PASSWORD}    myPassword
${continue}        //input[@id='continue']



*** Test Cases ***
Login Test
    [Tags]    Smoke
    Open Browsers    ${URL}    ${BROWSER}
    Sleep    10s
    Open Browsers    ${URL1}    ${BROWSER}
    # Open Browsers
    Click Login Button
    Input USERNAME
    Click Continue Button    ${continue}

LogOut Test
    Opne Setting aapp

   
    

*** Keywords ***
Open Browsers
    [Arguments]    ${abc}    ${xyz}
    Open Browser    ${abc}    ${xyz}
    


Input USERNAME
    Input Text    //Input[@id='ap_email']    ${USERNAME} 

Click Continue Button 
    [Arguments]    ${c_button}
    Click Button    ${continue}

Input Password
    Input Text    xpath=[span[@id=]]    ${PASSWORD}

Click Login Button
    Click Element    //span[@id='nav-link-accountList-nav-line-1'] 

Verify Successful Login
    Page Should Contain    text
    Close Browser

