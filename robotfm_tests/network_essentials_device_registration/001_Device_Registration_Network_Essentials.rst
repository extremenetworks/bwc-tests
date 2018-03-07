.. code:: robotframework


    *** Test Cases ***

    REGISTER CASTOR
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.register_device_credentials  mgmt_ip\=${CASTOR_IP}  username\=${CASTOR_USERNAME}  password\=${CASTOR_PASSWORD}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REGISTER FREEDOM
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.register_device_credentials  mgmt_ip\=${FREEDOM_IP}  username\=${FREEDOM_USERNAME}  password\=${FREEDOM_PASSWORD}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REGISTER CEDAR
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.register_device_credentials  mgmt_ip\=${CEDAR_IP}  username\=${CEDAR_USERNAME}  password\=${CEDAR_PASSWORD}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REGISTER USER INVALID
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.register_device_credentials  mgmt_ip\=${INVALID_IP}  username\=${INVALID_USERNAME}  password\=${INVALID_PASSWORD}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ERROR


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Variables           001_Device_Registration_Network_Essentials.yaml
