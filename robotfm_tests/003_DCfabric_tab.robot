*** Variables ***
${USERNAME}  st2admin
${PASSWORD}  st2admin

*** Settings ***
Library           Selenium2Library

*** Test Cases ***
Connect Webdriver
    ${service_args}=   Create List    -headless
    Create Webdriver   Chrome    ${service_args}
    Set Window Size    ${800}    ${600}

Login Page
    Go To  https://localhost/
    Input Text    name=username  ${USERNAME}
    Input Text    name=password  ${PASSWORD}

    # XPath for Connect Button as there is no unique locator
    Click Element   //html/body/div[1]/div[1]/form/div[2]/input
    Wait Until Element Is Visible  //html/body/div[1]/header/div[2]/a[2]  15  Seconds

    ${result}  Get Location
    Log To Console  \nURL: ${result}\n

Verify Suites Tab
    Click Element  //html/body/div[1]/header/div[2]/a[2]
    Wait Until Element Is Visible  //*[@id="st2-panel__scroller"]  10  Seconds

    ${result}  Get Location
    Log To Console  \nURL: ${result}\n

    [Teardown]  Close All Browsers
