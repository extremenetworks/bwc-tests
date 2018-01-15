.. code:: robotframework

    *** Keywords ***
    Connect Webdriver And Login
        [Arguments]    ${URL}  ${USERNAME}  ${PASSWORD}
        Log To Console     Connecting Webdriver....\n
        ${capabilities}    Evaluate  sys.modules['selenium.webdriver'].common.desired_capabilities.DesiredCapabilities.FIREFOX    sys,selenium.webdriver

        # For local UI test comment following line as "marionette" should be True for local
        Set To Dictionary  ${capabilities}    marionette=${False}

        Open Browser       ${URL}  firefox  capabilities=${capabilities}
        Set Window Size    ${1200}    ${700}

        Log To Console   Login to: ${URL}\n
        Input Text    name=username  ${USERNAME}
        Input Text    name=password  ${PASSWORD}

        # Temp fix for 2.5(Angular) and 2.6(react) UI
        ${version}=  Run Process  st2  --version
        Log To Console  Stackstorm version:-:-> ${version.stderr}
        ${ver}=  Set Variable If   "2.5" in "${version.stderr}"   2.5   2.6
        Set Global Variable    ${ST2_VERSION}  ${ver}
        Log To Console  \nST2 version to test UI: ${ST2_VERSION}\n

        # XPath for Connect Button as there is no unique locator
        Run Keyword If  ${ST2_VERSION}==2.6  Click Element   //*[@id="container"]/div/div/form/div[3]/input
        ...       ELSE  Click Element   //html/body/div[1]/div[1]/form/div[2]/input
        Log To Console  \nST2 version
        Run Keyword If  ${ST2_VERSION}==2.6  Wait Until Element Is Visible  //*[@id="container"]/div/div/header/div[2]/a[2]  15  Seconds
        ...       ELSE  Wait Until Element Is Visible  //html/body/div[1]/header/div[2]/a[2]  15  Seconds

        Log To Console  \nST2 version

    Login Page
        [Arguments]    ${URL}  ${USERNAME}  ${PASSWORD}
        Go To  ${URL}
        Input Text    name=username  ${USERNAME}
        Input Text    name=password  ${PASSWORD}

        # XPath for Connect Button as there is no unique locator
        Run Keyword If  ${ST2_VERSION}==2.6   Click Element   //*[@id="container"]/div/div/form/div[3]/input
        ...       ELSE  Click Element   //html/body/div[1]/div[1]/form/div[2]/input
        Run Keyword If  ${ST2_VERSION}==2.6   Wait Until Element Is Visible  //*[@id="container"]/div/div/header/div[2]/a[2]  15  Seconds
        ...       ELSE  Wait Until Element Is Visible   //html/body/div[1]/header/div[2]/a[2]  15  Seconds

        ${result}  Get Location
        Log To Console  \nLogin Successful - URL: ${result}\n

    *** Settings ***
    Library           Selenium2Library
    Library           Collections
