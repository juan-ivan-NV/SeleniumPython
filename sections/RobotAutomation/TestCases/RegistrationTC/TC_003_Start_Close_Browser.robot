*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot
Documentation  This file contains testcase of testing ABC Functionality 
Test Setup  Start Browser and Maximize
Test Teardown  Close Browser Window


*** Variables ***
${Browser}  Chrome
${Url}  https://www.thetestingworld.com/testings

*** Test Cases ***
Robot Third Test Case
    Input Text  name:fld_username  Testing
    Input Text  name:fld_email  123546
    Input Text  name:fld_password  45685

Robot Third Next Test Case
    Select Radio Button  add_type  office
