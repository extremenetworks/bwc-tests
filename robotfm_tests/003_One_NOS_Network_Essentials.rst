.. code:: robotframework

    *** Test Cases ***

    CREATE VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully created
        Should Contain   ${op}  Skipping to update Interface description

    CREATE VLAN DUPLICATE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  already exists, not created
        Should Contain   ${op}  Skipping to update Interface description

    CREATE VLAN WITH DESCRIPTION
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID2}  intf_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully created
        Should Contain   ${op}  Successfully updated VLAN description

    CREATE VLAN RANGE
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN RANGE}  intf_desc\=${VLAN DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully created
        Should Contain   ${op}  Successfully updated VLAN description

    SET L2 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L2 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l2_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L2 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set L2 mtu on device due to Incorrect mtu value


    SET L3 SYSTEM MTU
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L3 MTU}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    SET L3 SYSTEM MTU IPV6
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${SYSTEM L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Successfully  set  mtu_size

    SET L3 SYSTEM MTU IPV6 INVALID
        ${result}=       Run Process  st2  run  network_essentials.set_l3_system_mtu  mgmt_ip\=${SWITCH 1}  mtu_size\=${INVLAID L3 MTU IPV6}  afi\=ipv6
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Cannot set system IP mtu on device

    GET OS VERSION
        ${output}=       Run Process  st2  run  network_essentials.get_os_version  mgmt_ip\=${SWITCH 1}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  succeeded


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            resource.robot
    Suite Setup         resource.Clean NOSSwitch
    Variables           003_One_NOS_Network_Essentials.yaml
