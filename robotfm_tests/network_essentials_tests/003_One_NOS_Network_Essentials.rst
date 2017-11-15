.. code:: robotframework

    *** Test Cases ***

    CREATE VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

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
        Should Not Contain   ${op}  ERROR

    CREATE VLAN RESERVED
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=1002
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ERROR

    CREATE VLAN WITH DESCRIPTION
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID2}  vlan_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}  vlan_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE VLAN BIG RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN BIG RANGE}  vlan_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    SET L2 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L2 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set L2 mtu on device due to Incorrect mtu value


    SET L3 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    SET L3 SYSTEM MTU IPV6
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU IPV6 INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        #Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    SET L2 MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l2_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${L2 MTU}  intf_name\=${FORTY INTF NAME}   intf_type\=fortygigabitethernet 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L2 MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l2_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L2 MTU}  intf_name\=${FORTY INTF NAM E}   intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set L2 mtu

    SET L3 MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l3_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${L3 MTU}  intf_name\=${FORTY INTF NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L3 MTU}  intf_name\=${FORTY INTF NAME}  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set L3 mtu

    SET L3 MTU IPV6
        ${result}=       Run Process  st2  run  network_essentials.set_l3_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${L3 MTU}  intf_name\=${FORTY INTF NAME}  afi\=ipv6  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 MTU IPV6 INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVALID L3 MTU}  intf_name\=${FORTY INTF NAME}  afi\=ipv6  intf_type\=fortygigabitethernet
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set L3 mtu

    GET OS VERSION
        ${result}=       Run Process  st2  run  network_essentials.get_os_version  mgmt_ip\=${SWITCH 1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  succeeded



    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown      resource.Clean NOSSwitch_Network_Essentials
    Variables           003_One_NOS_Network_Essentials.yaml
    Variables           003_One_NOS_Network_Essentials_Message.yaml
