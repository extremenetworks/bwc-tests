.. code:: robotframework

    *** Test Cases ***
    Check Empty BWC List
        ${result}=        Run Process  bwc  ipf  inventory  list  --fabric\=default 
        Log To Console    \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc}
        Should Contain    ${result.stderr}  ${MSG LIST}
        Should Not Contain   ${result.stdout}   Fabric

    Register Switch in BWC server
        ${result}=      Run Process  bwc  ipf  inventory  register  fabric\=${FABRIC NAME}  host\=${IP ADDRESS}  user\=${USER}  passwd\=${PASSWD}  -f  yaml  
        Log To Console  \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc}
        Should Contain  ${result.stderr}  ${MSG ADD}
        Run Keyword     Inventory Should Contain  ${result}

    Update Switch in BWC server
        ${result}=      Run Process  bwc  ipf  inventory  update  --host\=${IP ADDRESS}  -f  yaml
        Log To Console  \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc} 
        Should Contain  ${result.stderr}  ${MSG UPDATE}
        Run Keyword     Inventory Should Contain  ${result}

    Check BWC List with one registered switch
        ${result}=      Run Process  bwc  ipf  inventory  list  --fabric\=${FABRIC NAME}  -f  yaml
        Log To Console  \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc}
        Should Contain  ${result.stderr}  ${MSG LIST}
        Run Keyword     Inventory Should Contain  ${result}

    Delete Switch from BWC server
        ${result}=      Run Process  bwc  ipf  inventory  delete  host\=${IP ADDRESS}  -f  yaml
        Log To Console  \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc}
        Should Contain  ${result.stderr}  ${MSG DELETE}
        Run Keyword     Inventory Should Contain  ${result}

    Check Empty BWC List Again
        ${result}=        Run Process  bwc  ipf  inventory  list  --fabric\=default
        Log To Console    \nOUTPUT:\n${result.stdout}\nERR:\n${result.stderr}\nRC:\n${result.rc}
        Should Contain    ${result.stderr}  ${MSG LIST}
        Should Not Contain   ${result.stdout}   Fabric


    *** Keywords ***
    Inventory Should Contain 
        [Arguments]     ${result}
        Should Contain  ${result.stdout}  - ASN: ${ASN}
        Should Contain  ${result.stdout}  Fabric: ${FABRIC NAME}
        Should Contain  ${result.stdout}  Firmware: ${FIRMWARE}
        Should Contain  ${result.stdout}  IP: ${IP ADDRESS}
        Should Contain  ${result.stdout}  Model: ${MODEL}
        Should Contain  ${result.stdout}  Name: ${SWITCH NAME}
        Should Contain  ${result.stdout}  Rbridge-Id: ${RBRIDGE}
        Should Contain  ${result.stdout}  Role: ${ROLE}    
    
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Variables           variables/001.yaml
    Resource            resource.robot
    # Suite Setup         resource.Clean Switches
    # Suite Teardown      Clean Switches
