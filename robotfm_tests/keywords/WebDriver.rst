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

        # XPath for Connect Button as there is no unique locator
        Click Element   //*[@id="container"]/div/div/form/div[3]/input
        Wait Until Element Is Visible  //*[@id="container"]/div/div/header/div[2]/a[2]  15  Seconds

        ${result}  Get Location
        Log To Console  \nLogin Successful - URL: ${result}\n

    Login Page
        [Arguments]    ${URL}  ${USERNAME}  ${PASSWORD}
        Go To  ${URL}
        Input Text    name=username  ${USERNAME}
        Input Text    name=password  ${PASSWORD}

        # XPath for Connect Button as there is no unique locator
        Click Element   //*[@id="container"]/div/div/form/div[3]/input
        Wait Until Element Is Visible  //*[@id="container"]/div/div/header/div[2]/a[2]  15  Seconds

        ${result}  Get Location
        Log To Console  \nLogin Successful - URL: ${result}\n

    *** Settings ***
    Library           Selenium2Library
    Library           Collections
