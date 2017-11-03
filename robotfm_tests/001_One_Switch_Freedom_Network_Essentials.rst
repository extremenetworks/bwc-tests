.. code:: robotframework


    *** Test Cases ***

    CREATE VLAN
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR
        
    CREATE VLAN LIST
        ${result}=       Run Process  st2  run  network_essentials.create_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN LIST}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR

    CONFIGURE SWITCHPORT ACCESS
		    ${result}=       Run Process  st2  run  network_essentials.create_switchport_access  mgmt_ip\=${SWITCH 1}  vlan_id\=${FRESH VLAN ID}  intf_name\=${ACCESS INTF NAME}  intf_type\=${INT TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_ACCESS_SUCCESS_MSG}
        
    CONFIGURE SWITCH PORT TRUNK
        ${result}=       Run Process  st2  run  network_essentials.create_switchport_trunk  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN LIST}  intf_name\=${TRUNK INTF NAME}  intf_type\=${INT TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}
        
    CREATE PORT CHANNEL DEFAULT INTLIST
        ${result}=       Run Process  st2  run  network_essentials.create_l2_port_channel  mgmt_ip\=${SWITCH 1}  intf_type\=${INT TYPE}  ports\=${PC SINGLEPRT}  port_channel_id\=${PO ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${PORT_CHANNEL_SUCCESS_MSG}
        
    CREATE PORT CHANNEL INVALID
        ${result}=       Run Process  st2  run  network_essentials.create_l2_port_channel  mgmt_ip\=${SWITCH 1}  intf_type\=${INT TYPE}  ports\=${PC SINGLEPRT}  port_channel_id\=po1
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${PORT_CHANNEL_INVALID_MSG}
        
        
    CREATE PORT CHANNEL NONDEFAULT
        ${result}=       Run Process  st2  run  network_essentials.create_l2_port_channel  mgmt_ip\=${SWITCH 1}  intf_type\=${INT TYPE}  ports\=${PC PRTLIST}  port_channel_id\=${PO ID3}  mode\=brocade  protocol\=modeon  port_channel_desc\=${PO DESC}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${PORT_CHANNEL_TYPE_SLX}
            
    VALIDATE PORT CHANNEL STATE
        ${result}=       Run Process  st2  run  network_essentials.validate_L2_port_channel_state  mgmt_ip\=${SWITCH 1}  port_channel_id\=${PO ID1} 
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${PORT_CHANNEL_OUTSYNC_MSG}
        
    DISABLE PORT CHANNEL
        ${result}=       Run Process  st2  run  network_essentials.set_intf_admin_state  mgmt_ip\=${SWITCH 1}  intf_type\=port_channel  intf_name\=${PO ID1}  enabled\=false  intf_desc\=portchannel
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should NOT Contain   ${op}  ERROR
        
    DELETE PORT CHANNEL DEFAULT INTLIST
        ${result}=       Run Process  st2  run  network_essentials.delete_l2_port_channel  mgmt_ip\=${SWITCH 1}  port_channel_id\=${PO ID1}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${PORT_CHANNEL_SUCCESS_MSG}
        
    REMOVE SWITCH PORT TRUNK VLAN
        ${result}=       Run Process  st2  run  network_essentials.remove_switchport_trunk_allowed_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN LIST}  intf_name\=${TRUNK INTF NAME}  intf_type\=${INT TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Contain   ${op}  ${SWITCHPORT_SUCCESS_MSG}
        
    DELETE SWITCHPORT
		    ${result}=       Run Process  st2  run  network_essentials.delete_switchport  mgmt_ip\=${SWITCH 1}  intf_name\=${ACCESS INTF NAME}  intf_type\=${INT TYPE}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should NOT Contain   ${op}  ERROR
        
    DELETE VLAN LIST
        ${result}=       Run Process  st2  run  network_essentials.delete_vlan  mgmt_ip\=${SWITCH 1}  vlan_id\=${VLAN LIST2}
        ${op}=           Get Variable Value  ${result.stdout}
        Log To Console   ${op}
        Should Not Contain   ${op}  ERROR  


    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            resource.robot
    Suite teardown      resource.Clean FreedomSwitch_Network_Essentials
    Variables           001_One_Switch_Freedom_Network_Essentials.yaml
    Variables           001_One_Switch_Network_Essentials_Message.yaml
