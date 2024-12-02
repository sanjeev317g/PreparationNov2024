*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}    https://practice.expandtesting.com/login
${continue}        //button[contains(text(),'Login')]

*** Test Cases ***
Data-Driven Test
    [Template]    Test with Data
    USERNAME    PASSWORD
    ABCDFDSFDFFDSFDF    204203948309284
    Blkdsjfdlsjfkls    08034975054594
    Csljfsdjflkdsfjldkjf    258405048504850



*** Keywords ***
Test with Data
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    ${BROWSER}
    Execute Javascript    window.scrollBy(0, 950)
    # Click Element    //span[@id='nav-link-accountList-nav-line-1'] 
    Input Text    //Input[@id='username']    ${username}
    Input Text    //input[@id='password']    ${password}
    Click Element    ${continue}
    