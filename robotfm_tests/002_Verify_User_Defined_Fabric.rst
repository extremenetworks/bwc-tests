.. code:: robotframework

    *** Test Cases ***
    List "default" Fabric
        ${output}=       Run Process  bwc  ipf  fabric  list 
        # --fabric=${FABRIC NAME} BUG: https://stackstorm.atlassian.net/browse/STORM-2340
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Fabric Name: ${FABRIC NAME}
        Should Contain   ${output.stdout}  bgp_multihop : ${BGP MULTIHOP}
        Should Contain   ${output.stdout}  spine_asn_block : ${SPINE ASN}
        Should Contain   ${output.stdout}  leaf_asn_block : ${LEAF ASN}
        Should Contain   ${output.stdout}  allowas_in : ${ALLOWAS IN}
        Should Contain   ${output.stdout}  max_paths : ${MAX PATHS}
        Should Contain   ${output.stdout}  bfd_multiplier : ${BFD MULTI}
        Should Contain   ${output.stdout}  p2p_link_range : ${P2P IP}
        Should Contain   ${output.stdout}  bfd_tx : ${BFD TX}
        Should Contain   ${output.stdout}  loopback_port_number : ${LOOPBACK PORT}
        Should Contain   ${output.stdout}  anycast_mac : ${ANYCAST MAC}
        Should Contain   ${output.stdout}  evpn_enabled : ${EVPN ENABLED}
        Should Contain   ${output.stdout}  loopback_ip_range : ${LOOPBACK IP}
        Should Contain   ${output.stdout}  bfd_rx : ${BFD RX}
  
    Add New Fabric: "${USER FABRIC}"
        ${output}=       Run Process   bwc  ipf  fabric  add  fabric\=${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}  Fabric ${USER FABRIC} Added successfully
        ${output}=       Run Process   bwc  ipf  fabric  add  fabric\=${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to add the fabric.${SPACE*2}Messages:\nFabric: ${USER FABRIC} already present.
        # Should Contain   Please run 'st2 execution get
  
    Add switch to a fabric without adding mandatory parameters should fail
        ${output}=      Run Process  bwc  ipf  inventory  register  fabric\=${USER FABRIC}  host\=${IP ADDRESS}  user\=${USER}  passwd\=${PASSWD}  -f  yaml  
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to register device.${SPACE*2}Messages:\nOne or more of the mandatory settings p2p_link_range, spine_asn_block, leaf_asn_block, loopback_ip_range, loopback_port_number have not been set for fabric ${USER FABRIC}
  
    Negative test case for mandatory parameters
        [Template]    BWC add fabric parameters TEMPLATE 
        p2p_link_range  wrong          ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        p2p_link_range  10             ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        p2p_link_range  1.1.1.256      ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        # p2p_link_range  1.1.1.1/20     ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_ip_range  wrong       ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_ip_range  10          ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_ip_range  1.1.1.256   ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        # loopback_ip_range  1.1.1.1/20  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  asd           ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  0             ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  asd-1         ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  1-4294967296  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  0-42          ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  42-4          ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block  4-4           ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_port_number  w        ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_port_number  0        ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_port_number  256      ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  asd            ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  0              ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  asd-1          ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  1-4294967296   ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  0-42           ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  42-4           ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block  4-4            ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
  
    Add mandatory parameters to the "${USER FABRIC}" for IP numbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        10.10.10.0/23    ${USER FABRIC}   Setting p2p_link_range with value 10.10.10.0/23 added to fabric fabric=${USER FABRIC}
        loopback_ip_range     172.32.254.0/24  ${USER FABRIC}   Setting loopback_ip_range with value 172.32.254.0/24 added to fabric fabric=${USER FABRIC}
        spine_asn_block       12-400           ${USER FABRIC}   Setting spine_asn_block with value 12-400 added to fabric fabric=${USER FABRIC}
        loopback_port_number  25               ${USER FABRIC}   Setting loopback_port_number with value 25 added to fabric fabric=${USER FABRIC}
        leaf_asn_block        500-660          ${USER FABRIC}   Setting leaf_asn_block with value 500-660 added to fabric fabric=${USER FABRIC}
  
    Add New Fabric: "unnumbered_fabric"
        ${output}=       Run Process   bwc  ipf  fabric   add   fabric\=${UNNUMBERED FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${UNNUMBERED FABRIC} Added successfully
  
    Add mandatory parameters to the "unnumbered_fabric" for IP unnumbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        unnumbered       ${UNNUMBERED FABRIC}   Setting p2p_link_range with value unnumbered added to fabric fabric=${UNNUMBERED FABRIC}
        loopback_ip_range     172.32.254.0/24  ${UNNUMBERED FABRIC}   Setting loopback_ip_range with value 172.32.254.0/24 added to fabric fabric=${UNNUMBERED FABRIC}
        spine_asn_block       4500-4900        ${UNNUMBERED FABRIC}   Setting spine_asn_block with value 4500-4900 added to fabric fabric=${UNNUMBERED FABRIC}
        loopback_port_number  25               ${UNNUMBERED FABRIC}   Setting loopback_port_number with value 25 added to fabric fabric=${UNNUMBERED FABRIC}
        leaf_asn_block        5000-6600        ${UNNUMBERED FABRIC}   Setting leaf_asn_block with value 5000-6600 added to fabric fabric=${UNNUMBERED FABRIC}
  
    Add New Fabric: "single_asn_fabric"
        ${output}=       Run Process   bwc  ipf  fabric   add   fabric\=${SINGLE FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${SINGLE FABRIC} Added successfully
  
    Add mandatory parameters to the "single_asn_fabric" for IP unnumbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        unnumbered       ${SINGLE FABRIC}   Setting p2p_link_range with value unnumbered added to fabric fabric=${SINGLE FABRIC}
        loopback_ip_range     172.32.254.0/24  ${SINGLE FABRIC}   Setting loopback_ip_range with value 172.32.254.0/24 added to fabric fabric=${SINGLE FABRIC}
        spine_asn_block       45000            ${SINGLE FABRIC}   Setting spine_asn_block with value 45000 added to fabric fabric=${SINGLE FABRIC}
        loopback_port_number  25               ${SINGLE FABRIC}   Setting loopback_port_number with value 25 added to fabric fabric=${SINGLE FABRIC}
        leaf_asn_block        50000            ${SINGLE FABRIC}   Setting leaf_asn_block with value 50000 added to fabric fabric=${SINGLE FABRIC}
  
    Check the mandatory values can not edited or deleted
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        10.10.10.0/23    ${USER FABRIC}   Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_ip_range     172.32.254.0/24  ${USER FABRIC}   Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block       12-400           ${USER FABRIC}   Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_port_number  25               ${USER FABRIC}   Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block        500-660          ${USER FABRIC}   Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        p2p_link_range        unnumbered       ${UNNUMBERED FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_ip_range     172.32.254.0/24  ${UNNUMBERED FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block       4000-4500        ${UNNUMBERED FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        loopback_port_number  25               ${UNNUMBERED FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block        5000-6600        ${UNNUMBERED FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        spine_asn_block       45000            ${SINGLE FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        leaf_asn_block        5000             ${SINGLE FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
  
  
    Switch registration should be successful now for all three fabrics "${USER FABRIC}", "unnumbered", "single_asn_fabric":
        Comment          A switch can be added only to one fabric on a server
        ${output}=    Inventory Register  ${UNNUMBERED FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${UNNUMBERED FABRIC}
        ${output}     Inventory Register  ${USER FABRIC}         10.24.39.225  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${USER FABRIC}
        ${output}=    Inventory Register  ${SINGLE FABRIC}      10.24.39.226  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${SINGLE FABRIC}
        ${result}=  Inventory Delete  10.24.39.224
        Should Contain  ${output.stdout}  Fabric: ${UNNUMBERED FABRIC}
        ${result}=  Inventory Delete  10.24.39.225
        Should Contain  ${output.stdout}  Fabric: ${USER FABRIC}
        ${result}=  Inventory Delete  10.24.39.226
        Should Contain  ${output.stdout}  Fabric: ${SINGLE FABRIC}
  
    Negative test case for other parameters
        [Template]    BWC add fabric parameters TEMPLATE
        anycast_mac   wrong  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:      
        anycast_mac   1234   ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        anycast_mac   10.10.10.10   ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        anycast_mac   wwww.wwww.wwww  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        anycast_mac   ffff.ffff.ffffe  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        anycast_mac   aa:aa:aa:aa:aa:ss  ${USER FABRIC}  Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_multiplier  0       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_multiplier  2       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_multiplier  51      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_multiplier  a       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_rx          00      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_rx          49      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_rx          30001   ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_rx          a       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_tx          00      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_tx          49      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_tx          30001   ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bfd_tx          a       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bgp_multihop    a       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bgp_multihop    0       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bgp_multihop    56      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        bgp_multihop    ''      ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        evpn_enabled    Y       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        evpn_enabled    N       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        evpn_enabled    0       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        max_paths       0       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        max_paths       a       ${USER FABRIC}          Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        max_paths       33       ${USER FABRIC}         Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
        max_paths       ""       ${USER FABRIC}         Operation failed:\nFailure Reason: Failed to add key value pair.${SPACE*2}Messages:
  
    Add other paramter to "${USER FABRIC}":
        [Template]    BWC add fabric parameters TEMPLATE
        anycast_mac   1234.4567.7890  ${USER FABRIC}   Setting anycast_mac with value 1234.4567.7890 added to fabric fabric=${USER FABRIC}
        bfd_multiplier  30            ${USER FABRIC}   Setting bfd_multiplier with value 30 added to fabric fabric=${USER FABRIC}
        bfd_rx          60            ${USER FABRIC}   Setting bfd_rx with value 60 added to fabric fabric=${USER FABRIC}
        bfd_tx          60            ${USER FABRIC}   Setting bfd_tx with value 60 added to fabric fabric=${USER FABRIC}
        bgp_multihop    50            ${USER FABRIC}   Setting bgp_multihop with value 50 added to fabric fabric=${USER FABRIC}
        evpn_enabled    Yes           ${USER FABRIC}   Setting evpn_enabled with value Yes added to fabric fabric=${USER FABRIC}
        max_paths       30            ${USER FABRIC}   Setting max_paths with value 30 added to fabric fabric=${USER FABRIC}
  
    # Verify "${USER FABRIC}" with all the parameters
    #     ${output}=       Run Process    bwc  ipf  fabric  list  \-\-fabric\=${USER FABRIC}
    #     Log To Console   OUTPUT: \n${output.stdout}
    #     Should Contain   ${output.stdout}   fabric_name: ${USER FABRIC}
    #     Should Contain   ${output.stdout}   fabric_settings:
    #     Should Contain   ${output.stdout}   anycast_mac: 1234.4567.7890
    #     Should Contain   ${output.stdout}   bfd_multiplier: '30'
    #     Should Contain   ${output.stdout}   bfd_rx: '60'
    #     Should Contain   ${output.stdout}   bfd_tx: '60'
    #     Should Contain   ${output.stdout}   bgp_multihop: '50'
    #     Should Contain   ${output.stdout}   evpn_enabled: 'Yes'
    #     Should Contain   ${output.stdout}   leaf_asn_block: 500-660
    #     Should Contain   ${output.stdout}   Setting loopback_ip_range with value 172.32.254.0/24 added to fabric fabric=${USER FABRIC}
    #     Should Contain   ${output.stdout}   loopback_port_number: '25'
    #     Should Contain   ${output.stdout}   max_paths: '30'
    #     Should Contain   ${output.stdout}   Setting p2p_link_range with value 10.10.10.0/23 added to fabric fabric=${USER FABRIC}
    #     Should Contain   ${output.stdout}   Setting spine_asn_block with value 12-400 added to fabric fabric=${USER FABRIC}
  
    Registration of switch MUST only happen after mandatory values are added to a fabric:
        ${output}=       Run Process   bwc  ipf  fabric   add   fabric\=${TEST FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${TEST FABRIC} Added successfully
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    p2p_link_range        10.10.10.0/23    ${TEST FABRIC}   Setting p2p_link_range with value 10.10.10.0/23 added to fabric fabric=${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    loopback_ip_range     172.32.254.0/24  ${TEST FABRIC}   Setting loopback_ip_range with value 172.32.254.0/24 added to fabric fabric=${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    spine_asn_block       1-2           ${TEST FABRIC}   Setting spine_asn_block with value 1-2 added to fabric fabric=${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    loopback_port_number  2               ${TEST FABRIC}   Setting loopback_port_number with value 2 added to fabric fabric=${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    leaf_asn_block        7-9          ${TEST FABRIC}   Setting leaf_asn_block with value 7-9 added to fabric fabric=${TEST FABRIC}
        ${output}=       Inventory Register  ${TEST FABRIC}  10.24.39.224  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${TEST FABRIC}
        # ${result}=  Inventory Delete  10.24.39.224
        # Should Contain  ${output.stdout}  Fabric: ${TEST FABRIC}
        ${output}=       Run Process   bwc  ipf  fabric  delete  ${TEST FABRIC}
        Should Contain   ${output.stderr}  Fabric ${TEST FABRIC} deleted successfully 

    Delete New Fabric: "${USER FABRIC}"
        ${output}=       Run Process   bwc  ipf  fabric  delete  ${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}  Fabric ${USER FABRIC} deleted successfully
        ${output}=       Run Process   bwc  ipf  fabric  delete  fabric\=${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to delete the fabric.${SPACE*2}Messages:\nFabric: ${USER FABRIC} does not exist.
        Should Contain   ${output.stdout}  Please run 'st2 execution get
  
    Delete the unnumbered and single ASN Fabric:
        ${output}=       Run Process   bwc  ipf  fabric  delete  ${SINGLE FABRIC}
         Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
         Should Contain   ${output.stderr}  Fabric ${SINGLE FABRIC} deleted successfully
         ${output}=       Run Process   bwc  ipf  fabric  delete  ${UNNUMBERED FABRIC}
         Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
         Should Contain   ${output.stderr}  Fabric ${UNNUMBERED FABRIC} deleted successfully
  
    Add and delete "default" fabric should fail
        ${output}=       Run Process   bwc  ipf  fabric   add   fabric\=${FABRIC NAME}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Cannot add a default fabric
        ${output}=       Run Process   bwc  ipf  fabric   delete   fabric\=${FABRIC NAME}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Cannot delete a default fabric
  
    Fabric config for non-existent fabric
        BWC add fabric parameters TEMPLATE     key       value    ${NO FABRIC}    Fabric: ${NO FABRIC} does not exist.
        BWC delete fabric parameters TEMPLATE  key                ${NO FABRIC}    Fabric: ${NO FABRIC} does not exist.
        BWC fabric config show TEMPLATE                           ${NO FABRIC}    Fabric does not exist: ${NO FABRIC}

    *** Keywords ***
    BWC add fabric parameters TEMPLATE
        [Arguments]      ${KEY}  ${VALUE}  ${FABRIC}  ${RESULT}
        ${output}=       Run Process  bwc  ipf  fabric  config  set  fabric\=${FABRIC}  ${KEY}  ${VALUE}
        Log To Console   ADD LOG: \n${output.stdout} \nRC: ${output.rc} \nERROR: ${output.stderr}
        Should Contain   ${output.stdout}  ${RESULT}
    BWC add fabric parameters TEMPLATE ERROR
        [Arguments]      ${KEY}  ${VALUE}  ${FABRIC}  ${RESULT}
        ${output}=       Run Process  bwc  ipf  fabric  config  set  fabric\=${FABRIC}  ${KEY}  ${VALUE}
        Log To Console   ADD LOG: \n${output.stdout} \nRC: ${output.rc} \nERROR: ${output.stderr}
        Should Contain   ${output.stderr}  ${RESULT}
    BWC delete fabric parameters TEMPLATE
        [Arguments]      ${KEY}  ${FABRIC}  ${RESULT}
        ${output}=       Run Process    bwc  ipf  fabric  config  delete  fabric\=${FABRIC}  ${KEY}
        Log To Console   DEL LOG: \n${output.stdout} \nRC: ${output.rc} \nERROR: ${output.stderr}
        Should Contain   ${output.stdout}  ${RESULT}
    BWC fabric config show TEMPLATE
        [Arguments]      ${FABRIC}  ${RESULT}
        ${output}=       Run Process    bwc  ipf  fabric  list   --fabric\=${FABRIC}
        Log To Console   SHOW LOG: \n${output.stdout} \nRC: ${output.rc} \nERROR: ${output.stderr}
        Should Contain   ${output.stdout}  ${RESULT}
    Inventory Register Fail
        [Arguments]     ${FABRIC NAME}  ${IP ADDRESS}  ${USER}  ${PASSWD}
        ${output}=      Run Process  bwc  ipf  inventory  register  fabric\=${FABRIC NAME}  host\=${IP ADDRESS}  user\=${USER}  passwd\=${PASSWD}  -f  yaml
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Return From Keyword  ${output}

    *** Variables ***
    ${FABRIC NAME}    default
    ${BGP MULTIHOP}   5
    ${SPINE ASN}      64512-64999
    ${LEAF ASN}       65000-65534
    ${ALLOWAS IN}     5
    ${MAX PATHS}      8
    ${BFD MULTI}      3
    ${P2P IP}         10.10.10.0/23
    ${BFD TX}         300
    ${LOOPBACK PORT}  1
    ${ANYCAST MAC}    aabb.ccdd.eeff
    ${EVPN ENABLED}   Yes
    ${LOOPBACK IP}    172.32.254.0/24
    ${BFD RX}         300

    ${USER FABRIC}        new_fabric
    ${SINGLE FABRIC}      single_asn_fabric
    ${UNNUMBERED FABRIC}  unnumbered_fabric
    ${NO FABRIC}          no_fabric
    ${TEST FABRIC}        test_fabric

    ${FAB_VAR_ADD_FAIL}   Failed to add key value pair.${SPACE*2}Messages:
    ${FAB_ADD_SUCCESS}    Successfully added the fabric.${SPACE*2}Object details:\nFabric: ${USER FABRIC}\n
    ${FAB_DEL_SUCCESS}    Successfully deleted the Fabric.${SPACE*2}Object details:\nFabric: ${USER FABRIC}\n
    ${FAB_ADD_FAIL}       Failed to add the fabric.${SPACE*2}Messages:\nFabric: ${USER FABRIC} already present.
    ${FAB_DEL_FAIL}       Failed to delete the fabric.${SPACE*2}Messages:\nFabric: new_fabric does not exist.
    ${SW_REG_FAIL}        One or more of the mandatory settings p2p_link_range, spine_asn_block, leaf_asn_block,
    ...                    loopback_ip_range, loopback_port_number have not been set for fabric new_fabric
    ${SW_REG_FAIL_TEST}   One or more of the mandatory settings p2p_link_range, spine_asn_block, leaf_asn_block,
    ...                    loopback_ip_range, loopback_port_number have not been set for fabric ${TEST FABRIC}
    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            resource.robot
    Resource            keywords/BwcInventory.rst
    Variables           001_One_Switch_Inventory_Operations.yaml
