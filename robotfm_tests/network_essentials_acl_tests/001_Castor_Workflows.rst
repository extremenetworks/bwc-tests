.. code:: robotframework    
	

    *** Test Cases ***
    
    CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  seq_id\=${SEQ_ID1}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH ETHERTYPE AND ANY SOURCE DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST5}  seq_id\=${SEQ_ID2}  ethertype\=${ETHERTYPE3}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}  intf\=${VDX INT NAME3}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK1}  seq_id\=${SEQ_ID3}  ethertype\=${ETHERTYPE2}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC, SRC_MAC_MASK AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  seq_id\=${SEQ_ID4}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH SOURCE_MAC, DESTINATION_MAC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}  intf\=${VDX INT NAME4}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK1}  destination\=${DEST1}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK3}  seq_id\=${SEQ_ID5}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID7}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH DESTINATION_MAC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK3}  seq_id\=${SEQ_ID6}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID5}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE, DESTINATION_MAC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK2}  seq_id\=${SEQ_ID7}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID6}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    NEGATIVE, DUPLICATE ENTRY, CREATE AND APPLY DROP PROVISION L2 RULE WITH ANY SOURCE, DESTINATION_MAC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCE5}  destination\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK2}  seq_id\=${SEQ_ID7}  ethertype\=${ETHERTYPE2}  vlan_id\=${VLAN ID6}
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "failed" in """${status}"""
	Should Be True		${res}
        


    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL AND ANY SOURCE DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTF}  protocol_type\=${PROTOCOL_TYPE4}  ethertype\=${ETHERTYPE}  seq_id\=${SEQ_ID1}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID5}  seq_id\=${SEQ_ID2}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL ICMP, SOURCE AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME1}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}  intf\=${VDX INT NAME3}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE3}  seq_id\=${SEQ_ID3}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, SOURCE AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEH}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID2}  seq_id\=${SEQ_ID4}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL TCP, SOURCE AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  seq_id\=${SEQ_ID5}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL TCP, SOURCE DOMAIN AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME2}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}  intf\=${VDX INT NAME4}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  ethertype\=${ETHERTYPE3}  vlan_id\=${VLAN ID1}  seq_id\=${SEQ_ID6}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL, DSCP, SOURCE AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEI}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP2}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID7}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE NTP AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME1}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}  intf\=${VDX INT NAME3}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEG}  destination\=${DESTC}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID4}  seq_id\=${SEQ_ID8}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE CHARGEN AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEC}  destination\=${DESTH}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP4}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID5}  seq_id\=${SEQ_ID9}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE SSDP AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME2}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}  intf\=${VDX INT NAME4}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCEE}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP3}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID2}  seq_id\=${SEQ_ID10}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PROTOCOL UDP, DSCP, SOURCE QOTD AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCED}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID11}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    NEGATIVE, DUPLICATE ENTRY, CREATE AND APPLY DROP PROVISION IPv4 RULE WITH PERMIT, PROTOCOL UDP, DSCP, SOURCE QOTD AND DESTINATION
        ${result}=       Run Process  st2  run  network_essentials.drop_provision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  intf\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  rule_action\=${ACTION}  source\=${SOURCED}  destination\=${DESTI}  protocol_type\=${PROTOCOL_TYPE1}  dscp\=${DSCP1}  ethertype\=${ETHERTYPE}  vlan_id\=${VLAN ID3}  seq_id\=${SEQ_ID12}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "failed" in """${status}"""
	Should Be True		${res}
        


    REMOVE AND DELETE L2 ACL, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  address_type\=${MAC_ADDR_TYPE}  delete_acl\=${DELETE_ACL}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    REMOVE AND DELETE L2 ACL1, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME1}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}  address_type\=${MAC_ADDR_TYPE}  delete_acl\=${DELETE_ACL}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    REMOVE AND DELETE L2 ACL2, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${MAC_ACL_NAME2}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}  address_type\=${MAC_ADDR_TYPE}  delete_acl\=${DELETE_ACL}  
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}



    REMOVE AND DELETE IPV4 ACL, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}  address_type\=${IPV4_ADDR_TYPE}  delete_acl\=${DELETE_ACL}    
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    REMOVE AND DELETE IPV4 ACL1, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME1}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}  address_type\=${IPV4_ADDR_TYPE}  delete_acl\=${DELETE_ACL}    
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}

    REMOVE AND DELETE IPV4 ACL2, RULES USING DROP UNPROVISION
        ${result}=       Run Process  st2  run  network_essentials.drop_unprovision  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPV4_ACL_NAME2}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}  address_type\=${IPV4_ADDR_TYPE}  delete_acl\=${DELETE_ACL}    
        Log To Console   ${result.stdout}
	${status}=     Get Lines Containing String  ${result.stdout}  status
        Log To Console   ${status}
	${res}=  Evaluate  "succeeded" in """${status}"""
	Should Be True		${res}


    DELETE SWITCHPORT FOR INTERFACE VDX INT NAME2
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE SWITCHPORT FOR INTERFACE VDX INT NAME3
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    DELETE SWITCHPORT FOR INTERFACE VDX INT NAME4
        ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME4}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
	
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Library             String
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           001_ACL.yaml
