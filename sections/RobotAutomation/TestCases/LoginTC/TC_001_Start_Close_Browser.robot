*** Settings ***
Library  ../../ExternalKeywords/Locators.py



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

*** Keywords ***
Read Element Locator
    [Arguments]  JsonPath
    ${result}=  read_locator_from_json  JsonPath
    [return]  ${result}
