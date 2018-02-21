.. code:: robotframework    
	
    *** Test Cases ***

    
    CREATE VRF1 AND ASSIGN IPv4 ADDRESS FAMILY
        [Tags]           skip-stable    
        ${result}=       Run Process  st2  run  network_essentials.create_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vrf_name\=${VRF_NAME1}  rbridge_id\=${RBRIDGE_ID}  afi\=${AFI_IPv4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VRF1 AND ASSIGN IPv6 ADDRESS FAMILY
        ${result}=       Run Process  st2  run  network_essentials.create_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vrf_name\=${VRF_NAME1}  rbridge_id\=${RBRIDGE_ID}  afi\=${AFI_IPv6}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VRF2 AND ASSIGN IPv4 ADDRESS FAMILY
        [Tags]           skip-stable    
        ${result}=       Run Process  st2  run  network_essentials.create_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vrf_name\=${VRF_NAME2}  rbridge_id\=${RBRIDGE_ID}  afi\=${AFI_IPv4}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VRF2 AND ASSIGN IPv6 ADDRESS FAMILY
        ${result}=       Run Process  st2  run  network_essentials.create_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vrf_name\=${VRF_NAME2}  rbridge_id\=${RBRIDGE_ID}  afi\=${AFI_IPv6}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE A VE1 AND ASSIGN TO VRF1
        ${result}=       Run Process  st2  run  network_essentials.create_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID1}  rbridge_id\=${RBRIDGE_ID}  vrf_name\=${VRF_NAME1}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE A VE2 AND ASSIGN TO VRF2
        ${result}=       Run Process  st2  run  network_essentials.create_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID2}  rbridge_id\=${RBRIDGE_ID}  vrf_name\=${VRF_NAME2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VE3 AND ASSIGN AN IP ADDRESS TO IT
        ${result}=       Run Process  st2  run  network_essentials.create_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID3}  rbridge_id\=${RBRIDGE_ID}  ip_address\=${IP_ADDR1}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VE4 AND ASSIGN AN IP ADDRESS TO IT
        ${result}=       Run Process  st2  run  network_essentials.create_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID4}  rbridge_id\=${RBRIDGE_ID}  ip_address\=${IP_ADDR2}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    CREATE VE5 WITH VE_ID AND ASSIGN AN IP ADDRESS TO IT
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.create_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID5}  rbridge_id\=${RBRIDGE_ID}  ve_id\=${VE_ID}  ip_address\=${IP_ADDR3}  
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VRF1
        ${result}=       Run Process  st2  run  network_essentials.delete_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vrf_name\=${VRF_NAME1}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VRF2
        ${result}=       Run Process  st2  run  network_essentials.delete_vrf  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vrf_name\=${VRF_NAME2}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VE1
        ${result}=       Run Process  st2  run  network_essentials.delete_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vlan_id\=${VLAN_ID1}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VE2
        ${result}=       Run Process  st2  run  network_essentials.delete_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vlan_id\=${VLAN_ID2}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VE3
        ${result}=       Run Process  st2  run  network_essentials.delete_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vlan_id\=${VLAN_ID3}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VE4
        ${result}=       Run Process  st2  run  network_essentials.delete_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vlan_id\=${VLAN_ID4}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VE5
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.delete_ve  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  rbridge_id\=${RBRIDGE_ID}  vlan_id\=${VLAN_ID5}  ve_id\=${VE_ID}      
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VLAN1
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID1}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VLAN2
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID2}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VLAN3
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID3}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VLAN4
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID4}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded

    DELETE VLAN5
        [Tags]           skip-stable
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${CASTOR_IP}  username\=${USERNAME}  password\=${PASSWORD}  vlan_id\=${VLAN_ID5}    
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        Should Contain   ${op}  succeeded


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Suite teardown         resource.Clean CastorSwitch_Network_Essentials
    Variables           005_VE_VRF.yaml

    
    
