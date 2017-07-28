.. code:: robotframework

    *** Test Cases ***

    CREATE VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_SUCCESS_MSG}
        Should Contain   ${op}  ${SKIPPING_VLAN}

    CREATE VLAN INVALID
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${INVALID VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Not a valid vlan123 

    CONFIGURE VF Enable
        ${result}=       Run Process  st2  run  network_essentials.configure_vf  mgmt_ip\=${SWITCH 1}  virtual_fabric_enable\=True
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Enabling VCS Virtual Fabric on the device 

    CREATE VF 
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully created a VLAN 
   
    SWITCH PORT TRUNK
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  intf_name\=${TRUNK INTF NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}

    DELETE VLAN
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op} is deleted 

    DELETE VF 
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op} is deleted 

    CONFIGURE VF Disable 
        ${result}=       Run Process  st2  run  network_essentials.configure_vf  mgmt_ip\=${SWITCH 1}  virtual_fabric_enable\=False
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Disabling VCS Virtual Fabric on the device 


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            resource.robot
    Suite Setup         resource.Clean NOSSwitch
    Variables           004_Virtual_Fabric_Operations.yaml 
    Variables           003_One_NOS_Network_Essentials_Message.yaml
