.. code:: robotframework

    *** Variables ***
    ${URL}        https://localhost/
    ${USERNAME}  st2admin
    ${PASSWORD}  st2admin

    *** Settings ***
    Library           Selenium2Library
    Library           Collections
    Library           Process
    Resource          ../keywords/WebDriver.rst
    Suite Setup       Connect Webdriver And Login  ${URL}  ${USERNAME}  ${PASSWORD}
    Suite Teardown    Close All Browsers

    *** Test Cases ***
    Test: Get st2 version
        ${version}=  Run Process  st2  --version
        Log To Console  Stackstorm version: ${version.stderr}
        ${ver}=  Set Variable If   "2.4" in "${version.stderr}"   2.4   2.5
        Set Global Variable    ${ST2_VERSION}    ${ver}
        Log To Console  \nST2 version: ${ST2_VERSION}\n

    Test: Verify Second tab is for Suites
        Click Element  //html/body/div[1]/header/div[2]/a[2]
        Wait Until Element Is Visible  //*[@id="st2-panel__scroller"]  10  Seconds
        ${result}  Get Location
        Should Contain  ${result}  suites
        Log To Console  \nSeccond Tab URL: ${result}\n

        # suites for v2.5
        Run Keyword If  ${ST2_VERSION}==2.5  Wait Until Element Is Visible  //html/body/div[1]/main/div[1]/div[2]/div[1][contains(text(), ' Suites ')]  10  Seconds
        # DC fabric for v2.4
        ...       ELSE  Wait Until Element Is Visible  //html/body/div[1]/main/div[1]/div[2]/div[1][contains(text(), ' DC Fabric: Actions ')]

    Test: Verify that the Groupings of Actions/Workflows shows up in the DC Fabric Tab
        Wait Until Element Is Visible   //html/body/div[1]/main/div[1]/div[3]/div/div[1]/div[1]/h4/span[contains(text(), ' DCFABRIC ')]
        Element Should Contain  //html/body/div[1]/main/div[1]/div[3]  Manage EVPN Tenants and Edge Ports
