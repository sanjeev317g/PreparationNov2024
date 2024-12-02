*** Settings ***
Library    selenium
Library    RPA.Browser.Selenium
Library    Collections
Library    RPA.SAP

*** Variables ***
${static}    Interview
${dynamic}   
${List}    [1,2,3,]
@{My List}    item1    item2

*** Test Cases ***
Launch Application
    Open Browser    https://www.flipkart.com/mobile-phones-store    chrome
    
    Click Link    Become a Seller

    Switch Window

    ${main_window}   Get Window Handles

    Set Selenium Implicit Wait    10

    Wait Until Element Is Visible    ""locator""
    FOR    ${element}    IN  ${main_window}  
        Log    List of the windows
        Log    ${element}
        
    END


   
   Log    ""Animal Animal ""


Dynamic Static Variables
    Insert Into List    ${My List}    1    new_item
    FOR    ${element}    IN    @{My LIST}
        Log    ${element}
    END

    
