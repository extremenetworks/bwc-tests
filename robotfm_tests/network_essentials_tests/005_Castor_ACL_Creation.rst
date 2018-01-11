.. code:: robotframework    
	
    *** Test Cases ***

    CREATE MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    CREATE MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${MAC_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${MAC_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE L2 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH DEST AND LOG ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  seq_id\=${SEQ_ID2}  action\=${ACTION}  dst\=${DEST1}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH VLAN ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID3}  action\=${ACTION}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC DEST AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCE2}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  count\=${COUNT}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCE3}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH DEST VLAN LOG AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID6}  action\=${ACTION}  dst\=${DEST3}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID2}  log\=${LOG}  count\=${COUNT}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC DEST AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  seq_id\=${SEQ_ID7}  action\=${ACTION1}  source\=${SOURCE4}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST4}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR



    CREATE IPv4 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCEA}  protocol_type\=${PROTOCOL_TYPE4}  destination\=${DESTF}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH DEST LOG AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  seq_id\=${SEQ_ID2}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE4}  count\=${COUNT}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH IP PROTOCOL_UDP ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID3}  action\=${ACTION}  source\=${SOURCEF}  protocol_type\=${PROTOCOL_TYPE1}  destination\=${DESTF}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH DEST, IP PROTOCOL S_PORT AND LOG
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCEG}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN, S_PORT AND COUNT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID6}  action\=${ACTION}  source\=${SOURCEB}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL AND D_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID7}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTC}  protocol_type\=${PROTOCOL_TYPE1}     
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN AND DSCP1
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID8}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP1}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC AND DEST (ICMP)
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  seq_id\=${SEQ_ID9}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTF}  protocol_type\=${PROTOCOL_TYPE3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE IPv4 ACL RULE WITH SRC, DEST AND IP PROTOCOL 
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  seq_id\=${SEQ_ID10}  action\=${ACTION}  source\=${SOURCEE}  destination\=${DESTE}  protocol_type\=${PROTOCOL_TYPE1} 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR		

    CREATE IPv4 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN3 AND DSCP3
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  seq_id\=${SEQ_ID11}  action\=${ACTION1}  source\=${SOURCEA}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP3}  vlan_id\=${VLAN_ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN1 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID12}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN2 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID13}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN4 AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID14}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN3 SYNC AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID15}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID3}  sync\=${SYNC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN5 RST AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID16}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID5}  rst\=${RST}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC, IP PROTOCOL, VLAN FIN AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID17}  action\=${ACTION1}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID}  fin\=${FIN}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN1 PUSH AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID18}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID1}  push\=${PUSH}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN2 ACK AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID19}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID2}  ack\=${ACK}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE IPv4 ACL RULE WITH SRC_E, IP PROTOCOL, VLAN3 URG AND S_PORT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID20}  action\=${ACTION1}  source\=${SOURCEE}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID3}  urg\=${URG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

		
    APPLY MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    APPLY IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    APPLY IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    
    REMOVE MAC_ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    REMOVE MAC_ACL1 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME1}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    
    REMOVE MAC_ACL2 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    
    REMOVE IPv4_ACL FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL1 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME1}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL2 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL3 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    REMOVE IPv4_ACL4 FROM INTERFACE
        ${result}=       Run Process  st2  run  network_essentials.remove_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}		
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR



    DELETE MAC_ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE MAC_ACL1
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE MAC_ACL2
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    DELETE IPv4_ACL
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL1
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL2
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE IPv4_ACL3
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    DELETE IPv4_ACL4
        ${result}=       Run Process  st2  run  network_essentials.delete_acl  mgmt_ip\=${CASTOR IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    

    CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  seq_id\=${SEQ_ID1}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH ETHERTYPE AND ANY SOURCE DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST5}  seq_id\=${SEQ_ID2}  ethertype\=${ETHERTYPE3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK1}  seq_id\=${SEQ_ID3}  ethertype\=${ETHERTYPE2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC, SRC_MAC_MASK AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  seq_id\=${SEQ_ID4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC, DESTINATION_MAC AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK1}  destination\=${DEST1}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK3}  seq_id\=${SEQ_ID5}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID7}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH DESTINATION_MAC AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK3}  seq_id\=${SEQ_ID6}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID5}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE, DESTINATION_MAC AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK2}  seq_id\=${SEQ_ID7}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID6}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    NEGATIVE, DUPLICATE ENTRY, CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE, DESTINATION_MAC AND VLAN
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK2}  seq_id\=${SEQ_ID7}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID6}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR



    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL AND ANY SOURCE DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTF}  protocol_type\=${PROTOCOL_TYPE4}  ethertype\=${ETHERTYPE}  seq_id\=${SEQ_ID1}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID5}  seq_id\=${SEQ_ID2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL ICMP, SOURCE AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE3}  seq_id\=${SEQ_ID3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, SOURCE AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEH}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID2}  seq_id\=${SEQ_ID4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL TCP, SOURCE AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  seq_id\=${SEQ_ID5}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL TCP, SOURCE DOMAIN AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  ethertype\=${ETHERTYPE3}  vlan_id\=${VLAN ID1}  seq_id\=${SEQ_ID6}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL, DSCP, SOURCE AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP2}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID7}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE NTP AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEG}  destination\=${DESTC}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID4}  seq_id\=${SEQ_ID8}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE CHARGEN AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEC}  destination\=${DESTH}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP4}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID5}  seq_id\=${SEQ_ID9}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE SSDP AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEE}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP3}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID2}  seq_id\=${SEQ_ID10}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE QOTD AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCED}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID11}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    NEGATIVE, DUPLICATE ENTRY, CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PERMIT, PROTOCOL UDP, DSCP, SOURCE QOTD AND DESTINATION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCED}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID12}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    REMOVE AND DELETE L2 ACL, RULES USING DROP UNPROVISION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  delete_acl\=${DELETE_ACL}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR


    REMOVE AND DELETE IPV4 ACL, RULES USING DROP UNPROVISION
        [Tags]           skip-unstable
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  delete_acl\=${DELETE_ACL}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

	
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           005_ACL.yaml
