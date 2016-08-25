.. code:: robotframework

    *** Variables ***
    ${MSG ADD}     Inventory Add
    ${MSG UPDATE}  Inventory Update
    ${MSG DELETE}  Inventory Delete
    ${MSG LIST}    Inventory List

    *** Keywords ***
    Inventory Should Contain
        [Arguments]     ${output}
        Should Contain  ${output.stdout}  - ASN: ${ASN}
        Should Contain  ${output.stdout}  Fabric: ${FABRIC NAME}
        Should Contain  ${output.stdout}  Firmware: ${FIRMWARE}
        Should Contain  ${output.stdout}  IP: ${IP ADDRESS}
        Should Contain  ${output.stdout}  Model: ${MODEL}
        Should Contain  ${output.stdout}  Name: ${SWITCH NAME}
        Should Contain  ${output.stdout}  Rbridge-Id: ${RBRIDGE}
        Should Contain  ${output.stdout}  Role: ${ROLE}

    Inventory Register
        [Arguments]     ${FABRIC NAME}  ${IP ADDRESS}  ${USER}  ${PASSWD}
        ${output}=      Run Process  bwc  ipf  inventory  register  fabric\=${FABRIC NAME}  host\=${IP ADDRESS}  user\=${USER}  passwd\=${PASSWD}  -f  yaml
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain  ${output.stderr}  ${MSG ADD}
        Return From Keyword  ${output}

    Inventory Update
        [Documentation]  Needs two args. However, FABRIC NAME and IP ADDRESS are mutually exclusive. Other must be ${FALSE}
        ...              Also ${USER} and {PASSWD} are optional.
        [Arguments]      ${FABRIC NAME}  ${IP ADDRESS}
        ${output}=       Run Keyword If  ${FABRIC NAME} == ${FALSE}  Run Process  bwc  ipf  inventory  update  --host\=${IP ADDRESS}  --user\=${USER}  --passwd\=${PASSWD}  -f  yaml
        ...              ELSE            Run Process  bwc  ipf  inventory  update  --fabric\=${FABRIC NAME}    --user\=${USER}  --passwd\=${PASSWD}  -f  yaml
        Log To Console   \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}  ${MSG UPDATE}
        Return From Keyword  ${output}

    Inventory Delete
        [Arguments]     ${IP ADDRESS}
        ${output}=      Run Process  bwc  ipf  inventory  delete  host\=${IP ADDRESS}  -f  yaml
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain  ${output.stderr}  ${MSG DELETE}
        Return From Keyword  ${output}

    Inventory List
        [Documentation]  Needs two args. However, FABRIC NAME and IP ADDRESS are mutually exclusive. Other must be ${FALSE}
        [Arguments]      ${FABRIC NAME}  ${IP ADDRESS}
        ${output}=       Run Keyword If  ${IP ADDRESS} == ${FALSE}   Run Process  bwc  ipf  inventory  list  --fabric\=${FABRIC NAME}  -f  yaml
        ...              ELSE            Run Process  bwc  ipf  inventory  list  --host\={IP ADDRESS}
        Log To Console    \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain    ${output.stderr}  ${MSG LIST}
        Return From Keyword  ${output}

    *** Settings ***
    Library             OperatingSystem
    Library             Process
