.. code:: robotframework

    *** Test Cases ***


    BWC WORKFLOW BGP SWITCHES SINGLE SPINE ASN
        #LEAF is Single Leaf ==> so  'allow_as_in 1" on leaf
        #VNI Enabled  ==> Overlay gateway has  auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_PEERGROUP  ADD SJ_FABRIC_SINGLE_ASN_BLOCK  ADD SJ_FABRIC_VLAN_VNI_AUTO
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}


        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'Yes'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'Yes'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI AUTO VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES SINGLE SPINE ASN VLAN VNI DISABLED
        #LEAF is Single Leaf ==> so  'allow_as_in 1" on leaf
        #VNI Disbaled  ==> Overlay gateway has no auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_PEERGROUP  ADD SJ_FABRIC_SINGLE_ASN_BLOCK
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI MANUAL VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES LEAF ASN BLOCK
        #LEAF has ASN Block ==> so no 'allow_as_in 1" on leaf
        #VNI Enabled  ==> Overlay gateway has auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_PEERGROUP  ADD SJ_FABRIC_LEAF_ASN_BLOCK  ADD SJ_FABRIC_VLAN_VNI_AUTO
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'Yes'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'Yes'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI AUTO VLAN

        #[Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES LEAF ASN BLOCK VNI DISABLED
        #LEAF has ASN Block ==> so no 'allow_as_in 1" on leaf
        #VNI Disabled  ==> Overlay gateway has no auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_PEERGROUP  ADD SJ_FABRIC_LEAF_ASN_BLOCK
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI MANUAL VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES SINGLE SPINE ASN NON PEER GROUP
        #LEAF is Single Leaf ==> so  'allow_as_in 1" on leaf
        #VNI Enabled  ==> Overlay gateway has  auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_SINGLE_ASN_BLOCK  ADD SJ_FABRIC_VLAN_VNI_AUTO
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'Yes'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'Yes'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI AUTO VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES SINGLE SPINE ASN VLAN VNI DISABLED NON PEER GROUP
        #LEAF is Single Leaf ==> so  'allow_as_in 1" on leaf
        #VNI Disbaled  ==> Overlay gateway has no auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_SINGLE_ASN_BLOCK
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI MANUAL VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES LEAF ASN BLOCK NON PEER GROUP
        #LEAF has ASN Block ==> so no 'allow_as_in 1" on leaf
        #VNI Enabled  ==> Overlay gateway has auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_LEAF_ASN_BLOCK  ADD SJ_FABRIC_VLAN_VNI_AUTO
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'Yes'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'Yes'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI AUTO VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX


    BWC WORKFLOW BGP SWITCHES LEAF ASN BLOCK VNI DISABLED NON PEER GROUP
        #LEAF has ASN Block ==> so no 'allow_as_in 1" on leaf
        #VNI Disabled  ==> Overlay gateway has no auto mapping
        [Setup]          Run Keywords  Create SJ_FABRIC_DEFAULT  ADD SJ_FABRIC_LEAF_ASN_BLOCK
        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_1}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Spine

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_2}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  inventory  register  ${SWITCH_3}  sj_fabric  admin  password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  Leaf

        ${result}=       Run Process  bwc  dcf  workflow  bgp  sj_fabric  All
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}

        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_ALL  ${SWITCH_3}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_SPINE  ${SWITCH_1}
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_BGP_NON_PEER_GROUP_ON_LEAF  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_2}  'No'
        ${result}=       Run Keyword   VERIFY_OVERLAY_GATEWAY  ${SWITCH_3}  'No'
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_EVPN_INSTANCE  ${SWITCH_3}

        ${result}=       Run Keyword   CONFIGURE L2 Tenant MAP VNI MANUAL VLAN

        [Teardown]       Run Keywords  Delete SJ_FABRIC_DEFAULT  Clean DCFabric_SLX

    *** Keywords ***

    VERIFY_BGP_NON_PEER_GROUP_ON_SPINE
        [Arguments]      ${SWITCH}
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config router bgp
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config router bgp  -i ${SWITCH}  -u admin  -p password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain X Times  ${op}  encapsulation vxlan  2
        Should Contain X Times  ${op}  local-as  1
        Should Contain X Times  ${op}  capability as4-enable  1
        Should Contain X Times  ${op}  remote-as  2
        Should Contain X Times  ${op}  retain route-target all  1

    VERIFY_BGP_NON_PEER_GROUP_ON_LEAF
        [Arguments]      ${SWITCH}  ${ALLOW_AS_IN}='Yes'
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config router bgp
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config router bgp  -i ${SWITCH}  -u admin  -p password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain X Times  ${op}  encapsulation vxlan  1
        Should Contain X Times  ${op}  local-as  1
        Should Contain X Times  ${op}  capability as4-enable  1
        Should Contain X Times  ${op}  remote-as  1
        Should Contain X Times  ${op}  network  1
        Run Keyword If   ${ALLOW_AS_IN} == 'Yes'  Should Contain  ${op}  allowas-in 1

    VERIFY_BGP_ON_SPINE
        [Arguments]      ${SWITCH}
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config router bgp
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config router bgp  -i ${SWITCH}  -u admin  -p password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain X Times  ${op}  encapsulation vxlan  1
        Should Contain X Times  ${op}  local-as  1
        Should Contain X Times  ${op}  capability as4-enable  1
        Should Contain X Times  ${op}  remote-as  2
        Should Contain X Times  ${op}  retain route-target all  1

    VERIFY_BGP_ON_LEAF
        [Arguments]      ${SWITCH}  ${ALLOW_AS_IN}='Yes'
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config router bgp
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config router bgp  -i ${SWITCH}  -u admin  -p password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain X Times  ${op}  encapsulation vxlan  1
        Should Contain X Times  ${op}  local-as  1
        Should Contain X Times  ${op}  capability as4-enable  1
        Should Contain X Times  ${op}  remote-as  1
        Should Contain X Times  ${op}  network  1
        Run Keyword If   ${ALLOW_AS_IN} == 'Yes'  Should Contain  ${op}  allowas-in 1

    VERIFY_OVERLAY_GATEWAY
        [Arguments]      ${SWITCH}  ${VNI_AUTO}='Yes'
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config overlay-gateway
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config overlay-gateway  -i ${SWITCH}  -u admin  -p password
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  overlay-gateway
        Should Contain   ${op}  layer2-extension
        Run Keyword If   ${VNI_AUTO} == 'Yes'  Should Contain   ${op}  map vni auto
        Should Contain   ${op}  ip interface Loopback
        Should Contain   ${op}  activate

    VERIFY_EVPN_INSTANCE
        [Arguments]      ${SWITCH}
        #${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config evpn
        ${result}=       Run Process   python    setup_teardown/switch_command.py  -c show running-config evpn  -i ${SWITCH}  -u admin  -p password

        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  route-target both auto ignore-as
        Should Contain   ${op}  rd auto

    VERIFY COMMON BGP
        [Arguments]      ${op}
        # "vxlan encapsulation" when evpn is turned on SLX
        Should Contain X Times  ${op}  neighbor spine_group encapsulation vxlan  2
        Should Contain X Times  ${op}  neighbor leaf_group encapsulation vxlan  1
        Should Contain X Times  ${op}  local-as  3
        Should Contain X Times  ${op}  capability as4-enable  3
        Should Contain X Times  ${op}  neighbor spine_group peer-group  2
        Should Contain X Times  ${op}  neighbor leaf_group peer-group  1
        Should Contain X Times  ${op}  network  2
        Should Contain X Times  ${op}  neighbor spine_group remote-as  2
        Should Contain X Times  ${op}  retain route-target all  1

    VERIFY COMMON BGP NON PEER GROUP
        [Arguments]      ${op}
        # "vxlan encapsulation" when evpn is turned on SLX
        Should Contain X Times  ${op}  encapsulation vxlan  4
        Should Contain X Times  ${op}  local-as  3
        Should Contain X Times  ${op}  capability as4-enable  3
        Should Contain X Times  ${op}  network  2
        Should Contain X Times  ${op}  remote-as  4
        Should Contain X Times  ${op}  retain route-target all  1


    VERIFY OVERLAY GATEWAY VNI DISABLED
        [Arguments]      ${SWITCH}
        ${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show running-config overlay-gateway
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  overlay-gateway
        Should Contain   ${op}  layer2-extension
        Should Not Contain   ${op}  map vni auto
        Should Contain   ${op}  ip interface Loopback
        Should Contain   ${op}  activate


    VERIFY_TUNNEL_STATUS
        [Arguments]      ${SWITCH}
        ${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=show tunnel brief
        ${op}=           Get Variable Value  ${result.stdout}
        Should Contain   ${op}  Admin state up, Oper state up

    CLEAR_BGP_ALL
        [Arguments]      ${SWITCH}
        ${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=clear ip bgp neighbor all
        ${op}=           Get Variable Value  ${result.stdout}

    CLEAR_BGP_EVPN_SOFT_IN
        [Arguments]      ${SWITCH}
        ${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=clear bgp evpn neighbor all soft in
        ${op}=           Get Variable Value  ${result.stdout}

    CLEAR_BGP_EVPN_SOFT_OUT
        [Arguments]      ${SWITCH}
        ${result}=       Run Process   st2  run  network_essentials.execute_cli  mgmt_ip\=${SWITCH}  cli_cmd\=clear bgp evpn neighbor all soft-outbond
        ${op}=           Get Variable Value  ${result.stdout}

    CONFIGURE L2 Tenant MAP VNI AUTO VLAN
        ${result}=       Run Process  st2  run  dcfabric.add_singlehomed_endpoint  mgmt_ip\=${SWITCH_2}  vlan_id\=${VLAN ID}  intf_name\=${INTF NAME}  intf_type\=${INTF TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_ACCESS_SUCCESS_MSG}
        ${result}=       Run Process  st2  run  dcfabric.add_singlehomed_endpoint  mgmt_ip\=${SWITCH_3}  vlan_id\=${VLAN ID}  intf_name\=${INTF NAME}  intf_type\=${INTF TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_ACCESS_SUCCESS_MSG}
        ${result}=       Run Process  st2  run  dcfabric.create_l2_tenant_evpn  mgmt_ip\=${SWITCH_2}  vlan_id\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR
        ${result}=       Run Process  st2  run  dcfabric.create_l2_tenant_evpn  mgmt_ip\=${SWITCH_3}  vlan_id\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR

        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_IN  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_OUT  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_IN  ${SWITCH_3}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_OUT  ${SWITCH_3}
        Sleep 1.5
        ${result}=       Run Keyword   VERIFY_TUNNEL_STATUS  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_TUNNEL_STATUS  ${SWITCH_3}

    CONFIGURE L2 Tenant MAP VNI MANUAL VLAN
        ${result}=       Run Process  st2  run  dcfabric.add_multihomed_endpoint  mgmt_ip\=${SWITCH_2}  vlan_id\=${VLAN ID}  ports\=${INTF NAME}  intf_type\=${INTF TYPE}  auto_pick_port_channel_id\=True  vni\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_TRUNK_SUCCESS_MSG}
        ${result}=       Run Process  st2  run  dcfabric.add_multihomed_endpoint  mgmt_ip\=${SWITCH_3}  vlan_id\=${VLAN ID}  ports\=${INTF NAME}  intf_type\=${INTF TYPE}  auto_pick_port_channel_id\=True  vni\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_TRUNK_SUCCESS_MSG}
        ${result}=       Run Process  st2  run  dcfabric.create_l2_tenant_evpn  mgmt_ip\=${SWITCH_2}  vlan_id\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR
        ${result}=       Run Process  st2  run  dcfabric.create_l2_tenant_evpn  mgmt_ip\=${SWITCH_3}  vlan_id\=${VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should not Contain   ${op}  ERROR

        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_IN  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_OUT  ${SWITCH_2}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_IN  ${SWITCH_3}
        ${result}=       Run Keyword   CLEAR_BGP_EVPN_SOFT_OUT  ${SWITCH_3}
        Sleep 1.5
        ${result}=       Run Keyword   VERIFY_TUNNEL_STATUS  ${SWITCH_2}
        ${result}=       Run Keyword   VERIFY_TUNNEL_STATUS  ${SWITCH_3}

    Delete SJ_FABRIC_DEFAULT
       ${result}=       Run Process  bwc  dcf  fabric   delete  sj_fabric

    Create SJ_FABRIC_DEFAULT
           ${result}=       Run Process  bwc  dcf  fabric   add  sj_fabric
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   vtep_loopback_port_number  2
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   p2p_link_range   10.10.10.0/23
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   evpn_enabled  Yes
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   loopback_ip_range  12.12.12.0/24
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   loopback_port_number  1

    ADD SJ_FABRIC_PEERGROUP
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   spine_peer_group  leaf_group
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   leaf_peer_group  spine_group

    ADD SJ_FABRIC_SINGLE_ASN_BLOCK
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   spine_asn_block  65200
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   leaf_asn_block  65208-65400

    ADD SJ_FABRIC_VLAN_VNI_AUTO
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   vni_auto_map  Yes

    ADD SJ_FABRIC_LEAF_ASN_BLOCK
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   spine_asn_block  65200
           ${result}=       Run Process  bwc  dcf  fabric   config  set  sj_fabric   leaf_asn_block  65208-65400

    EXECUTE_CMD_ON_SWITCH
          ${result}=       Run Process   python  setup_teardown/switch_command.py  -c "show running-config overlay-gateway" -i 10.24.39.252 -u admin -p password

    Clean DCFabric_SLX 
       Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Log To console   Suite setup and Teardown: Cleaning Switches!!!
       ${result}=       Run Process   python         setup_teardown/NOS_clean_fabric.py   -f  005_DCFabric_SLX
       Log To Console   Return Code: ${result.rc}
       # Uncomment the following lines it Return code is not 0
       Log To Console   all output:\n ${result.stdout}
       # Log To Console   err: ${result.stderr}
       Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    *** Settings ***

    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite Setup         resource.Clean DCFabric_SLX 
    Suite Teardown      resource.Clean DCFabric_SLX 
    Variables           005_DCFabric_SLX.yaml
