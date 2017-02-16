.. code:: robotframework

    *** Test Cases ***

    CREATE VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_SUCCESS_MSG}
        Should Contain   ${op}  ${SKIPPING_VLAN}

    CREATE VLAN INVALID VLAN ID
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${INVALID VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${NOT_VALID_VLAN}

    CREATE VLAN INVALID VLAN ID RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${INVALID VLAN RANGE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_INVALID}

    CREATE VLAN DUPLICATE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${ALREADY_EXISTS}
        Should Contain   ${op}  ${SKIPPING_VLAN}

    CREATE VLAN WITH DESCRIPTION
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID2}  intf_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_SUCCESS_MSG}
        Should Contain   ${op}  ${VLAN_UPDATE_DESC}

    CREATE VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}  intf_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${VLAN_SUCCESS_MSG}
        Should Contain   ${op}  ${VLAN_UPDATE_DESC}

    SWITCH PORT TRUNK
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  intf_name\=${TRUNK INTF NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}

    SWITCH PORT TRUNK DUPLICATE
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  intf_name\=${TRUNK INTF NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_CONFIG_EXISTS}

    SWITCH PORT TRUNK FORTY INVALID VLAN ID
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${NOT EXISTING VLAN ID}  intf_name\=${FORTY INTF NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_VLAN_NA}

    SWITCH PORT TRUNK FORTY INVALID NAME
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${NOT EXISTING VLAN ID}  intf_name\=${FORTY INTF INV NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_VLAN_NA}


    SWITCH PORT TRUNK FORTY
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  intf_name\=${FORTY INTF NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}




    SET L2 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L2 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set L2 mtu on device due to Incorrect mtu value


    SET L3 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    SET L3 SYSTEM MTU IPV6
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU IPV6 INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    GET OS VERSION
        ${result}=       Run Process  st2  run  network_essentials.get_os_version  mgmt_ip\=${SWITCH 1}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  succeeded


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            resource.robot
    Suite Setup         resource.Clean NOSSwitch
    Variables           003_One_NOS_Network_Essentials.yaml
    Variables           003_One_NOS_Network_Essentials_Message.yaml