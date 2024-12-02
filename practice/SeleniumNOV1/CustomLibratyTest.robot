*** Settings ***
Library    CustomLibrary.py

*** Variables ***

*** Test Cases ***
Multply Test
    ${result}=    multiply    3    4
    Should Be Equal As Numbers    ${result}    12


*** Keywords ***