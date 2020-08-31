*** Settings ***
Resource  ../../Resources/Resources1.robot
Test Setup  Start Browser and Maximize

*** Variables ***
${Browser}  Chrome
${Url}  https://www.thetestingworld.com/testings

*** Test Cases ***
Robot Fetch Data
    Create Folder at Runtime
    Start Browser and Maximize

