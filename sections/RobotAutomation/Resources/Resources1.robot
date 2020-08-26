*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***
Start Browser and Maximize
    Open Browser  https://www.thetestingworld.com/testings/  Chrome
    Maximize Browser Window

Close Browser Window
    ${Title}=  Get Title
    Log  ${Title}
    Close Browser

Before Each Test Suite
    Log  Before Each Test Suite

After Each Test Suite
    Log  After Each Test Suite 
