.. code:: robotframework


    *** Test Cases ***

    REMOVE ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
		
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           005_ACL.yaml 
