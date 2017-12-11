.. code:: robotframework


    *** Test Cases ***

    CREATE ACL
        ${result}=       Run Process  st2  run  network_essentials.create_acl  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  address_type\=${ADDR_TYPE}  acl_type\=${ACL_TYPE}  acl_name\=${ACL_NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE L2 ACL RULE WITH SRC ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID1}  action\=${ACTION}  source\=${SOURCE1}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CREATE L2 ACL RULE WITH DEST ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID2}  action\=${ACTION}  dst\=${DEST1}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH VLAN ONLY
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID3}  action\=${ACTION}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC AND DEST
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID4}  action\=${ACTION}  source\=${SOURCE2}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST2}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID5}  action\=${ACTION}  source\=${SOURCE3}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID3}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
    CREATE L2 ACL RULE WITH DEST AND VLAN 
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID6}  action\=${ACTION}  dst\=${DEST3}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    CREATE L2 ACL RULE WITH SRC DEST AND VLAN
        ${result}=       Run Process  st2  run  network_essentials.add_or_remove_l2_acl_rule  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  seq_id\=${SEQ_ID7}  action\=${ACTION}  source\=${SOURCE4}  src_mac_addr_mask\=${SRC_MAC_ADDR_MASK}  dst\=${DEST4}  dst_mac_addr_mask\=${DEST_MAC_ADDR_MASK}  ethertype\=${ETHERTYPE}  vlan\=${VLAN ID4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

	
    APPLY ACL
        ${result}=       Run Process  st2  run  network_essentials.apply_acl  mgmt_ip\=${SWITCH IP}  username\=${USERNAME}  password\=${PASSWORD}  acl_name\=${ACL_NAME}  acl_direction\=${DIRECTION}  intf_type\=${INT TYPE}  intf_name\=${INT NAME}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
		
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           005_Freedom_ACL.yaml 
