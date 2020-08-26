*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resources1.robot

*** Variables ***
${Browser}  Chrome
${Url}  https://www.thetestingworld.com/testings/ 

*** Test Cases ***
Robot First Test Case
    ${Res}=  Start Browser and Maximize  ${Url}  ${Browser}
    Log  ${Res}
    Input Text  name:fld_username  ${Res}
