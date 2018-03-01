.. code:: robotframework

    *** Test Cases ***


    CONFIGURE VF Enable
        ${result}=       Run Process  st2  run  network_essentials.enable_vf  mgmt_ip\=${SWITCH 1}  virtual_fabric_enable\=True
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Enabling VCS Virtual Fabric on the device 

    CREATE CTAG VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE VF VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
   
    SWITCH PORT TRUNK
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}  c_tag\=${FRESH VLAN ID}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}

    REMOVE SWITCH PORT TRUNK VLAN
        ${result}=       Run Process  st2  run  network_essentials.remove_switchport_trunk_allowed_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}  c_tag\=${FRESH VLAN ID}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}

    SWITCH PORT TRUNK INVALID VLANS
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  c_tag\=${FRESH VF ID}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ERROR

    DELETE SWITCH PORT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${SWITCH 1}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR

    CREATE CTAG VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}  vlan_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE VF VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VF VLAN RANGE}  vlan_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    SWITCH PORT TRUNK RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${VF VLAN RANGE}  c_tag\=${VLAN RANGE}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}

    DELETE SWITCH PORT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${SWITCH 1}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR

    CREATE MAC GROUP
        ${result}=       Run Process  st2  run  network_essentials.configure_mac_group  mgmt_ip\=${SWITCH 1}  mac_group_id\=${MAC GROUP ID}  mac_address\=${MAC ADDRESS}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${MAC_GROUP_SUCCESS_MSG}

    CONFIGURE SWITCH PORT ACCESS VLAN MAC CLASSIFICATION
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${SWITCH 1}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet  vlan_id\=${FRESH VLAN ID}  mac_group_id\=${MAC GROUP ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_ACCESS_SUCCESS_MSG}

    CONFIGURE SWITCH PORT ACCESS VLAN MAC CLASSIFICATION INVALID
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${SWITCH 1}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet  vlan_id\=${FRESH VF ID}  mac_group_id\=${MAC GROUP ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${MAC_GROUP_ASSOCIATION_MSG} 

    DELETE SWITCH PORT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${SWITCH 1}  intf_name\=${TRUNK INTF NAME}  intf_type\=tengigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR

    CONFIGURE VLAN TO VNI MAPPING
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  dcfabric.configure_vni_mapping  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  vlan_vni\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_VNI_MAP_SUCCESS_MSG}

    CONFIGURE VLAN TO VNI RANGE MAPPING
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  dcfabric.configure_vni_mapping  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}  vlan_vni\=${VF VLAN RANGE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_VNI_MAP_SUCCESS_MSG}

    DELETE VLAN TO VNI MAPPING
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  dcfabric.delete_vni_mapping  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_VNI_MAP_SUCCESS_MSG}

    DELETE VLAN TO VNI RANGE MAPPING
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  dcfabric.delete_vni_mapping  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_VNI_MAP_SUCCESS_MSG}

    DELETE VLAN TO VNI AUTO MAPPING
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  dcfabric.delete_vni_mapping  mgmt_ip\=${SWITCH 1}  auto\=True
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_VNI_MAP_SUCCESS_MSG}

    DELETE CTAG VLAN
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE VF VLAN
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VF ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE CTAG VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE VF VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VF VLAN RANGE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CONFIGURE VF Disable 
        ${result}=       Run Process  st2  run  network_essentials.enable_vf  mgmt_ip\=${SWITCH 1}  virtual_fabric_enable\=False
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Disabling VCS Virtual Fabric on the device 


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite Setup         resource.Clean NOSSwitch_Virtual_Fabric
    Suite Teardown      resource.Clean NOSSwitch_Virtual_Fabric
    Variables           004_One_NOS_Virtual_Fabric.yaml 
