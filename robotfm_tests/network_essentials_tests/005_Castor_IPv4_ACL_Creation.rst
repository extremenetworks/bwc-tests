.. code:: robotframework    
	
    *** Test Cases ***

    CREATE ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${IPv4_ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${IPv4_ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE L3 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCEA}  protocol_type\=${PROTOCOL_TYPE4}  destination\=${DESTF}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH DEST ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID2}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE4}  count\=${COUNT}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH IP PROTOCOL ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID3}  action\=${ACTION}  source\=${SOURCEF}  protocol_type\=${PROTOCOL_TYPE1}  destination\=${DESTF}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH DEST, IP PROTOCOL AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCEG}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE1}  log\=${LOG}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC, IP PROTOCOL, VLAN AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCEC}  protocol_type\=${PROTOCOL_TYPE2}  destination\=${DESTF}  count\=${COUNT}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC, DEST, IP PROTOCOL AND S_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID6}  action\=${ACTION}  source\=${SOURCEB}  destination\=${DESTA}  protocol_type\=${PROTOCOL_TYPE2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC, DEST, IP PROTOCOL AND D_PORT
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID7}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTC}  protocol_type\=${PROTOCOL_TYPE1}     
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC, DEST, IP PROTOCOL, D_PORT, VLAN AND DSCP
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID8}  action\=${ACTION}  source\=${SOURCEA}  destination\=${DESTB}  protocol_type\=${PROTOCOL_TYPE2}  dscp\=${DSCP1}  vlan_id\=${VLAN_ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC AND DEST (ICMP)
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID9}  action\=${ACTION}  source\=${SOURCEF}  destination\=${DESTF}  protocol_type\=${PROTOCOL_TYPE3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L3 ACL RULE WITH SRC, DEST AND IP PROTOCOL 
        ${result}=       Run Process  st2  run  network_essentials.add_ipv4_rule_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  seq_id\=${SEQ_ID10}  action\=${ACTION}  source\=${SOURCEE}  destination\=${DESTE}  protocol_type\=${PROTOCOL_TYPE1} 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR		
		
    APPLY ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${IPv4_ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${VDX INT TYPE}  intf_name\=${VDX INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           005_ACL.yaml
