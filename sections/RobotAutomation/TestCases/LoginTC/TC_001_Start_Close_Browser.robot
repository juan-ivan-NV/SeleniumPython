*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resources/Resources1.robot
Documentation  This file contains testcase of testing ABC Functionality 
Test Setup  Start Browser and Maximize
Test Teardown  Close Browser Window
Suite Setup  Before Each Test Suite



*** Variables ***
${Browser}  Chrome
${Url}  https://www.thetestingworld.com/testings

*** Test Cases ***
Robot First Test Case
    Input Text  name:fld_username  Testing
    Input Text  name:fld_email  123546
    Input Text  name:fld_password  45685

Robot Next Test Case
    Select Radio Button  add_type  office
