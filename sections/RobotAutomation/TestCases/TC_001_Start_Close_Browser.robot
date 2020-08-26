*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://www.facebook.com/

*** Test Cases ***
TC_001 Browser Start and Close
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window  
    Input Text  id:email  hello
    Input Text  id:pass  Abcd
    Click Button  xpath://button[@type="submit"]
    Click Link  xpath://a[text()="¿Olvidaste tu cuenta?"]
    #Close Browser  
