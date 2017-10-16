.. code:: robotframework

    *** Variables ***
    ${URL}        https://localhost/
    ${USERNAME}  st2admin
    ${PASSWORD}  st2admin

    *** Settings ***
    Library           Selenium2Library
    Library           Collections
    Resource          ../keywords/WebDriver.rst
    Suite Setup       Connect Webdriver And Login  ${URL}  ${USERNAME}  ${PASSWORD}
    Suite Teardown    Close All Browsers

    *** Test Cases ***
    Test: Verify Suites Tab
        Click Element  //html/body/div[1]/header/div[2]/a[2]
        Wait Until Element Is Visible  //*[@id="st2-panel__scroller"]  10  Seconds

        ${result}  Get Location
        Log To Console  \nURL: ${result}\n
