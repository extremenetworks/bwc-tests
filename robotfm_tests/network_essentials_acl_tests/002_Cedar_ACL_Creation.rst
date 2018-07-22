.. code:: robotframework    
	
    *** Test Cases ***

    CREATE MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    CREATE MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPV6_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPV6_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPV6_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPV6_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPV6_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPV6_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6_ACL3
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPV6_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPV6_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6_ACL4
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPV6_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPV6_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR




    CREATE L2 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH DEST AND LOG ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  seq_id\=${SEQ_ID2}  action\=${ACTION}  dst\=${DEST1}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH VLAN ONLY
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID3}  action\=${ACTION}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC DEST AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCE2}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  count\=${COUNT}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCE3}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH DEST VLAN LOG AND COUNT
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID6}  action\=${ACTION}  dst\=${DEST3}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID2}  log\=${LOG}  count\=${COUNT}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC DEST AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID7}  action\=${ACTION1}  source\=${SOURCE4}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST4}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR



    CREATE IPv4 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCEA}  protocol_type\=${PROTOCOL_TYPE4}  destination\=${DESTF}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH DEST LOG AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  seq_id\=${SEQ_ID2}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE4}  count\=${COUNT}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH IP PROTOCOL_UDP ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID3}  action\=${ACTION}  source\=${SOURCEF}  protocol_type\=${PROTOCOL_TYPE1}  destination\=${DESTF}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH DEST, IP PROTOCOL S_PORT AND LOG
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCEG}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  log\=${LOG}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN, S_PORT AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID6}  action\=${ACTION}  source\=${SOURCEB}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL AND D_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID7}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTC}  protocol_type\=${PROTOCOL_TYPE1}       
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN AND DSCP1
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID8}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP1}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC AND DEST (ICMP)
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID9}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTF}  protocol_type\=${PROTOCOL_TYPE3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST AND IP PROTOCOL 
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID10}  action\=${ACTION}  source\=${SOURCEE}  destination\=${DESTE}  protocol_type\=${PROTOCOL_TYPE1} 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR		

    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN3 AND DSCP3
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID11}  action\=${ACTION1}  source\=${SOURCEA}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP3}  vlan_id\=${VLAN_ID3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN1 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID12}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN2 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID13}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN4 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID14}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN3 SYNC AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID15}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID3}  sync\=${SYNC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN5 RST AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID16}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID5}  rst\=${RST}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN FIN AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID17}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID}  fin\=${FIN}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN1 PUSH AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID18}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID1}  push\=${PUSH}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN2 ACK AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID19}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID2}  ack\=${ACK}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN3 URG AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID20}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID3}  urg\=${URG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    
		
    CREATE IPv6 ACL RULE WITH IP PROTOCOL ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}  seq_id\=${SEQ_ID3}  action\=${ACTION}  source\=${SOURCE16}  protocol_type\=${PROTOCOL_TYPE5}  destination\=${DEST16}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH DEST, IP PROTOCOL AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCE17}  destination\=${DEST11}  protocol_type\=${PROTOCOL_TYPE1}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL VLAN AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC, DEST, IP PROTOCOL AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}  seq_id\=${SEQ_ID6}  action\=${ACTION}  source\=${SOURCE12}  destination\=${DEST11}  protocol_type\=${PROTOCOL_TYPE2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC, DEST, IP PROTOCOL AND D_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}  seq_id\=${SEQ_ID7}  action\=${ACTION}  source\=${SOURCE11}  destination\=${DEST13}  protocol_type\=${PROTOCOL_TYPE1}     
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT VLAN AND DSCP
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}  seq_id\=${SEQ_ID8}  action\=${ACTION}  source\=${SOURCE11}  destination\=${DEST12}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP1}  vlan_id\=${VLAN_ID}   
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC AND DEST (ICMP)
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}  seq_id\=${SEQ_ID9}  action\=${ACTION}  source\=${SOURCE16}  destination\=${DEST16}  protocol_type\=${PROTOCOL_TYPE6}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv6 ACL RULE WITH SRC, DEST AND IP PROTOCOL
        [Tags]           skip-stable 
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}  seq_id\=${SEQ_ID10}  action\=${ACTION}  source\=${SOURCE15}  destination\=${DEST15}  protocol_type\=${PROTOCOL_TYPE1} 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR		

    CREATE IPv6 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN AND DSCP1
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}  seq_id\=${SEQ_ID11}  action\=${ACTION1}  source\=${SOURCE11}  destination\=${DEST12}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP3}  vlan_id\=${VLAN_ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID12}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT1
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID13}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT2
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID14}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT3
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID15}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT4
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID16}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID5}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT5
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID17}  action\=${ACTION1}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT6
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID18}  action\=${ACTION}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT7
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID19}  action\=${ACTION}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv6 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT8
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv6_rule_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  seq_id\=${SEQ_ID20}  action\=${ACTION}  source\=${SOURCE13}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DEST16}  count\=${COUNT}  vlan_id\=${VLAN_ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    CREATE SWITCHPORT FOR INTERFACE TO APPLY MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}  vlan_id\=${VLAN_ID10}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    APPLY MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    

    CREATE SWITCHPORT FOR INTERFACE TO APPLY MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}  vlan_id\=${VLAN_ID10}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR    

    APPLY MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE SWITCHPORT FOR INTERFACE TO APPLY MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}  vlan_id\=${VLAN_ID10}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    APPLY IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

   
    APPLY IPv6_ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME5}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv6_ACL1
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME6}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv6_ACL2
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME7}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv6_ACL3
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME8}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv6_ACL4
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME9}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    
    REMOVE MAC_ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE SWITCHPORT FOR INTERFACE WHERE MAC_ACL WAS PRESENT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    REMOVE MAC_ACL1 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    DELETE SWITCHPORT FOR INTERFACE WHERE MAC_ACL1 WAS PRESENT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE MAC_ACL2 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    DELETE SWITCHPORT FOR INTERFACE WHERE MAC_ACL2 WAS PRESENT
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR    

    
    REMOVE IPv4_ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL1 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME1}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL2 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME2}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL3 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME3}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL4 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME4}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    REMOVE IPv6_ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME5}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv6_ACL1 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME6}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv6_ACL2 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME7}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv6_ACL3 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME8}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv6_ACL4 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${SLX INT TYPE}  intf_name\=${SLX INT NAME9}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR




    DELETE MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    DELETE IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    DELETE IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    DELETE IPv6_ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv6_ACL1
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv6_ACL2
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv6_ACL3
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv6_ACL4
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CEDAR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV6_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    
	
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           001_ACL.yaml
