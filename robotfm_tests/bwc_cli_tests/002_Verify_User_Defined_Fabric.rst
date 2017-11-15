.. code:: robotframework

    *** Test Cases ***
    List "default" Fabric
        ${output}=       Run Process  bwc  dcf  fabric  list
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

    Add New Fabric: "new_fabric"
        ${output}=       Run Process   bwc  dcf  fabric  add  fabric\=${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}  Fabric ${USER FABRIC} Added successfully
        ${output}=       Run Process   bwc  dcf  fabric  add  fabric\=${USER FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to add the fabric.${SPACE*2}Messages:\nFabric: ${USER FABRIC} already present.

    Add switch to a fabric without adding mandatory parameters should fail
        ${output}=      Run Process  bwc  dcf  inventory  register  fabric\=${USER FABRIC}  host\=${IP ADDRESS}  user\=${USER}  passwd\=${PASSWD}  -f  yaml
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to register device.${SPACE*2}Messages:\nOne or more of the mandatory settings p2p_link_range, spine_asn_block, leaf_asn_block, loopback_ip_range, loopback_port_number have not been set for fabric ${USER FABRIC} Also if evpn_enabled is Yes then vtep_loopback_port_number fabric setting has to be set

    Negative test case for mandatory parameters
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        wrong        ${USER FABRIC}  ${OPERATION FAILED}
        p2p_link_range        10           ${USER FABRIC}  ${OPERATION FAILED}
        p2p_link_range        1.1.1.256    ${USER FABRIC}  ${OPERATION FAILED}
        p2p_link_range        1.1.1.1/20   ${USER FABRIC}  ${OPERATION FAILED}
        loopback_ip_range     wrong        ${USER FABRIC}  ${OPERATION FAILED}
        loopback_ip_range     10           ${USER FABRIC}  ${OPERATION FAILED}
        loopback_ip_range     1.1.1.256    ${USER FABRIC}  ${OPERATION FAILED}
        loopback_ip_range     1.1.1.1/20   ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       asd           ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       0             ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       asd-1         ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       1-4294967296  ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       0-42          ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       42-4          ${USER FABRIC}  ${OPERATION FAILED}
        spine_asn_block       4-4           ${USER FABRIC}  ${OPERATION FAILED}
        loopback_port_number  w             ${USER FABRIC}  ${OPERATION FAILED}
        loopback_port_number  0             ${USER FABRIC}  ${OPERATION FAILED}
        loopback_port_number  256           ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        asd           ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        0             ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        asd-1         ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        1-4294967296  ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        0-42          ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        42-4          ${USER FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        4-4           ${USER FABRIC}  ${OPERATION FAILED}

    Add mandatory parameters to the "new_fabric" for IP numbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        ${USER P2P IP}              ${USER FABRIC}   Setting p2p_link_range with value ${USER P2P IP} added to fabric ${USER FABRIC}
        loopback_ip_range     ${USER LOOPBACK IP}         ${USER FABRIC}   Setting loopback_ip_range with value ${USER LOOPBACK IP} added to fabric ${USER FABRIC}
        spine_asn_block       ${USER SPINE ASN}           ${USER FABRIC}   Setting spine_asn_block with value ${USER SPINE ASN} added to fabric ${USER FABRIC}
        loopback_port_number  ${USER LOOPBACK PORT}       ${USER FABRIC}   Setting loopback_port_number with value ${USER LOOPBACK PORT} added to fabric ${USER FABRIC}
        leaf_asn_block        ${USER LEAF ASN}            ${USER FABRIC}   Setting leaf_asn_block with value ${USER LEAF ASN} added to fabric ${USER FABRIC}

    Add New Fabric: "unnumbered_fabric"
        ${output}=       Run Process   bwc  dcf  fabric   add   fabric\=${UNNUMBERED FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${UNNUMBERED FABRIC} Added successfully

    Add mandatory parameters to the "unnumbered_fabric" for IP unnumbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        ${UNNUMBERED P2P IP}         ${UNNUMBERED FABRIC}   Setting p2p_link_range with value ${UNNUMBERED P2P IP} added to fabric ${UNNUMBERED FABRIC}
        loopback_ip_range     ${UNNUMBERED LOOPBACK IP}    ${UNNUMBERED FABRIC}   Setting loopback_ip_range with value ${UNNUMBERED LOOPBACK IP} added to fabric ${UNNUMBERED FABRIC}
        spine_asn_block       ${UNNUMBERED SPINE ASN}      ${UNNUMBERED FABRIC}   Setting spine_asn_block with value ${UNNUMBERED SPINE ASN} added to fabric ${UNNUMBERED FABRIC}
        loopback_port_number  ${UNNUMBERED LOOPBACK PORT}  ${UNNUMBERED FABRIC}   Setting loopback_port_number with value ${UNNUMBERED LOOPBACK PORT} added to fabric ${UNNUMBERED FABRIC}
        leaf_asn_block        ${UNNUMBERED LEAF ASN}       ${UNNUMBERED FABRIC}   Setting leaf_asn_block with value ${UNNUMBERED LEAF ASN} added to fabric ${UNNUMBERED FABRIC}
        mct_link_ip_range     ${UNNUMBERED MCT IP}         ${UNNUMBERED FABRIC}   Setting mct_link_ip_range with value ${UNNUMBERED MCT IP} added to fabric ${UNNUMBERED FABRIC}
    Add New Fabric: "single_asn_fabric"
        ${output}=       Run Process   bwc  dcf  fabric   add   fabric\=${SINGLE FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${SINGLE FABRIC} Added successfully

    Add mandatory parameters to the "single_asn_fabric" for IP unnumbered
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        ${SINGLE P2P IP}         ${SINGLE FABRIC}   Setting p2p_link_range with value ${SINGLE P2P IP} added to fabric ${SINGLE FABRIC}
        loopback_ip_range     ${SINGLE LOOPBACK IP}    ${SINGLE FABRIC}   Setting loopback_ip_range with value ${SINGLE LOOPBACK IP} added to fabric ${SINGLE FABRIC}
        spine_asn_block       ${SINGLE SPINE ASN}      ${SINGLE FABRIC}   Setting spine_asn_block with value ${SINGLE SPINE ASN} added to fabric ${SINGLE FABRIC}
        loopback_port_number  ${SINGLE LOOPBACK PORT}  ${SINGLE FABRIC}   Setting loopback_port_number with value ${SINGLE LOOPBACK PORT} added to fabric ${SINGLE FABRIC}
        leaf_asn_block        ${SINGLE LEAF ASN}       ${SINGLE FABRIC}   Setting leaf_asn_block with value ${SINGLE LEAF ASN} added to fabric ${SINGLE FABRIC}
        mct_link_ip_range     ${SINGLE MCT IP}         ${SINGLE FABRIC}   Setting mct_link_ip_range with value ${SINGLE MCT IP} added to fabric ${SINGLE FABRIC}

    Check the mandatory values can not edited or deleted
        [Template]    BWC add fabric parameters TEMPLATE
        p2p_link_range        ${USER P2P IP}               ${USER FABRIC}        ${OPERATION FAILED}
        loopback_ip_range     ${USER LOOPBACK IP}          ${USER FABRIC}        ${OPERATION FAILED}
        spine_asn_block       ${USER LEAF ASN}             ${USER FABRIC}        ${OPERATION FAILED}
        loopback_port_number  ${USER LOOPBACK PORT}        ${USER FABRIC}        ${OPERATION FAILED}
        leaf_asn_block        ${USER SPINE ASN}            ${USER FABRIC}        ${OPERATION FAILED}
        p2p_link_range        ${UNNUMBERED P2P IP}         ${UNNUMBERED FABRIC}  ${OPERATION FAILED}
        loopback_ip_range     ${UNNUMBERED LOOPBACK IP}    ${UNNUMBERED FABRIC}  ${OPERATION FAILED}
        spine_asn_block       ${UNNUMBERED LEAF ASN}       ${UNNUMBERED FABRIC}  ${OPERATION FAILED}
        loopback_port_number  ${UNNUMBERED LOOPBACK PORT}  ${UNNUMBERED FABRIC}  ${OPERATION FAILED}
        leaf_asn_block        ${UNNUMBERED SPINE ASN}      ${UNNUMBERED FABRIC}  ${OPERATION FAILED}
        spine_asn_block       ${SINGLE LEAF ASN}           ${SINGLE FABRIC}      ${OPERATION FAILED}
        leaf_asn_block        ${SINGLE SPINE ASN}          ${SINGLE FABRIC}      ${OPERATION FAILED}


    Switch registration should be successful now for all three fabrics "new_fabric", "${UNNUMBERED P2P IP}", "single_asn_fabric":
        Comment          A switch can be added only to one fabric on a server
        ${output}=  Inventory Register  ${UNNUMBERED FABRIC}  ${SWITCH 1}  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${UNNUMBERED FABRIC}
        ${output}   Inventory Register  ${USER FABRIC}    ${SWITCH 2}  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${USER FABRIC}
        ${output}=  Inventory Register  ${SINGLE FABRIC}  ${SWITCH 3}  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${SINGLE FABRIC}
        ${output}=  Inventory Delete    ${SWITCH 1}
        Should Contain  ${output.stdout}  Fabric: ${UNNUMBERED FABRIC}
        ${output}=  Inventory Delete    ${SWITCH 2}
        Should Contain  ${output.stdout}  Fabric: ${USER FABRIC}
        ${output}=  Inventory Delete    ${SWITCH 3}
        Should Contain  ${output.stdout}  Fabric: ${SINGLE FABRIC}

    Negative test case for other parameters
        [Template]    BWC add fabric parameters TEMPLATE
        anycast_mac     wrong              ${USER FABRIC}  ${OPERATION FAILED}
        anycast_mac     1234               ${USER FABRIC}  ${OPERATION FAILED}
        anycast_mac     10.10.10.10        ${USER FABRIC}  ${OPERATION FAILED}
        anycast_mac     wwww.wwww.wwww     ${USER FABRIC}  ${OPERATION FAILED}
        anycast_mac     ffff.ffff.ffffe    ${USER FABRIC}  ${OPERATION FAILED}
        anycast_mac     aa:aa:aa:aa:aa:ss  ${USER FABRIC}  ${OPERATION FAILED}
        bfd_multiplier  0                  ${USER FABRIC}  ${OPERATION FAILED}
        bfd_multiplier  2                  ${USER FABRIC}  ${OPERATION FAILED}
        bfd_multiplier  51                 ${USER FABRIC}  ${OPERATION FAILED}
        bfd_multiplier  a                  ${USER FABRIC}  ${OPERATION FAILED}
        bfd_rx          00                 ${USER FABRIC}  ${OPERATION FAILED}
        bfd_rx          49                 ${USER FABRIC}  ${OPERATION FAILED}
        bfd_rx          30001              ${USER FABRIC}  ${OPERATION FAILED}
        bfd_rx          a                  ${USER FABRIC}  ${OPERATION FAILED}
        bfd_tx          00                 ${USER FABRIC}  ${OPERATION FAILED}
        bfd_tx          49                 ${USER FABRIC}  ${OPERATION FAILED}
        bfd_tx          30001              ${USER FABRIC}  ${OPERATION FAILED}
        bfd_tx          a                  ${USER FABRIC}  ${OPERATION FAILED}
        bgp_multihop    a                  ${USER FABRIC}  ${OPERATION FAILED}
        bgp_multihop    0                  ${USER FABRIC}  ${OPERATION FAILED}
        bgp_multihop    56                 ${USER FABRIC}  ${OPERATION FAILED}
        bgp_multihop    ''                 ${USER FABRIC}  ${OPERATION FAILED}
        evpn_enabled    Y                  ${USER FABRIC}  ${OPERATION FAILED}
        evpn_enabled    N                  ${USER FABRIC}  ${OPERATION FAILED}
        evpn_enabled    0                  ${USER FABRIC}  ${OPERATION FAILED}
        max_paths       0                  ${USER FABRIC}  ${OPERATION FAILED}
        max_paths       a                  ${USER FABRIC}  ${OPERATION FAILED}
        max_paths       33                 ${USER FABRIC}  ${OPERATION FAILED}
        max_paths       ""                 ${USER FABRIC}  ${OPERATION FAILED}

    Add other paramter to "new_fabric":
        [Template]  BWC add fabric parameters TEMPLATE
        anycast_mac     ${USER ANYCAST MAC}  ${USER FABRIC}   Setting anycast_mac with value ${USER ANYCAST MAC} added to fabric ${USER FABRIC}
        bfd_multiplier  ${USER MAX PATHS}    ${USER FABRIC}   Setting bfd_multiplier with value ${USER MAX PATHS} added to fabric ${USER FABRIC}
        bfd_rx          ${USER BFD RX}       ${USER FABRIC}   Setting bfd_rx with value ${USER BFD RX} added to fabric ${USER FABRIC}
        bfd_tx          ${USER BFD TX}       ${USER FABRIC}   Setting bfd_tx with value ${USER BFD TX} added to fabric ${USER FABRIC}
        bgp_multihop    ${USER BFD MULTI}    ${USER FABRIC}   Setting bgp_multihop with value ${USER BFD MULTI} added to fabric ${USER FABRIC}
        evpn_enabled    Yes                  ${USER FABRIC}   Setting evpn_enabled with value Yes added to fabric ${USER FABRIC}
        max_paths       ${USER MAX PATHS}    ${USER FABRIC}   Setting max_paths with value ${USER MAX PATHS} added to fabric ${USER FABRIC}

    Verify "new_fabric" with all the parameters
        ${output}=       Run Process        bwc  dcf  fabric  list  \-\-fabric\=${USER FABRIC}
        Log To Console   OUTPUT: \n${output.stdout}
        Should Contain   ${output.stdout}   Fabric Name: ${USER FABRIC}
        Should Contain   ${output.stdout}   anycast_mac : ${USER ANYCAST MAC}
        Should Contain   ${output.stdout}   bfd_multiplier : ${USER MAX PATHS}
        Should Contain   ${output.stdout}   bfd_rx : ${USER BFD RX}
        Should Contain   ${output.stdout}   bfd_tx : ${USER BFD TX}
        Should Contain   ${output.stdout}   bgp_multihop : ${USER BFD MULTI}
        Should Contain   ${output.stdout}   evpn_enabled : Yes
        Should Contain   ${output.stdout}   leaf_asn_block : ${USER LEAF ASN}
        Should Contain   ${output.stdout}   loopback_port_number : ${USER LOOPBACK PORT}
        Should Contain   ${output.stdout}   max_paths : ${USER MAX PATHS}

    Registration of switch MUST only happen after mandatory values are added to a fabric:
        ${output}=       Run Process   bwc  dcf  fabric   add   fabric\=${TEST FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stderr}   Fabric ${TEST FABRIC} Added successfully
        ${output}=       Inventory Register Fail   ${TEST FABRIC}  ${SWITCH 1}  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE  p2p_link_range         ${TEST P2P IP}        ${TEST FABRIC}   Setting p2p_link_range with value ${TEST P2P IP} added to fabric ${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}   ${SWITCH 1}  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE  loopback_ip_range      ${TEST LOOPBACK IP}   ${TEST FABRIC}   Setting loopback_ip_range with value ${TEST LOOPBACK IP} added to fabric ${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}   ${SWITCH 1}  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE  spine_asn_block        ${TEST SPINE ASN}     ${TEST FABRIC}   Setting spine_asn_block with value ${TEST SPINE ASN} added to fabric ${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  ${SWITCH 1}  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE  loopback_port_number  ${TEST LOOPBACK PORT}  ${TEST FABRIC}   Setting loopback_port_number with value 2 added to fabric ${TEST FABRIC}
        ${output}=       Inventory Register Fail  ${TEST FABRIC}  ${SWITCH 1}  ${USER}  ${PASSWD}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   ${SW_REG_FAIL_TEST}
        BWC add fabric parameters TEMPLATE    leaf_asn_block      ${TEST LEAF ASN}       ${TEST FABRIC}   Setting leaf_asn_block with value ${TEST LEAF ASN} added to fabric ${TEST FABRIC}
        BWC add fabric parameters TEMPLATE    mct_link_ip_range   ${TEST MCT IP}         ${TEST FABRIC}   Setting mct_link_ip_range with value ${TEST MCT IP} added to fabric ${TEST FABRIC}
        ${output}=       Inventory Register  ${TEST FABRIC}       ${SWITCH 1}  ${USER}  ${PASSWD}
        Should Contain  ${output.stdout}  Fabric: ${TEST FABRIC}
        ${output}=       Run Process   bwc  dcf  fabric  delete  ${TEST FABRIC}
        Should Contain   ${output.stderr}  Fabric ${TEST FABRIC} deleted successfully

    Delete New Fabric: "new_fabric"
      ${output}=       Run Process   bwc  dcf  fabric  delete  ${USER FABRIC}
      Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
      Should Contain   ${output.stderr}  Fabric ${USER FABRIC} deleted successfully
      ${output}=       Run Process   bwc  dcf  fabric  delete  fabric\=${USER FABRIC}
      Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
      Should Contain   ${output.stdout}  Operation failed:\nFailure Reason: Failed to delete the fabric.${SPACE*2}Messages:\nFabric: ${USER FABRIC} does not exist.
      Should Contain   ${output.stdout}  Please run 'st2 execution get

    Delete the unnumbered and single ASN Fabric:
        ${output}=       Run Process   bwc  dcf  fabric  delete  ${SINGLE FABRIC}
         Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
         Should Contain   ${output.stderr}  Fabric ${SINGLE FABRIC} deleted successfully
         ${output}=       Run Process   bwc  dcf  fabric  delete  ${UNNUMBERED FABRIC}
         Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
         Should Contain   ${output.stderr}  Fabric ${UNNUMBERED FABRIC} deleted successfully

    Add and delete "default" fabric should fail
        ${output}=       Run Process   bwc  dcf  fabric   add   fabric\=${FABRIC NAME}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Cannot add a default fabric
        ${output}=       Run Process   bwc  dcf  fabric   delete   fabric\=${FABRIC NAME}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Cannot delete a default fabric

    Fabric config for non-existent fabric
        ${output}=       Run Process   bwc  dcf  fabric   config  set  fabric\=${NO FABRIC}  key\=loopback_port_number  value\=1
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Fabric: ${NO FABRIC} does not exist.
        ${output}=       Run Process  bwc  dcf  fabric   config  delete  fabric\=${NO FABRIC}  key\=loopback_port_number
        Log To Console   DEL LOG: \n${output.stdout} \nRC: ${output.rc} \nERROR: ${output.stderr}
        Should Contain   ${output.stdout}   Fabric: ${NO FABRIC} does not exist.
        ${output}=       Run Process   bwc  dcf  fabric  config  show  fabric\=${NO FABRIC}
        Log To Console  \nOUTPUT:\n${output.stdout}\nERR:\n${output.stderr}\nRC:\n${output.rc}
        Should Contain   ${output.stdout}   Fabric does not exist: ${NO FABRIC}

    *** Settings ***
    Library             OperatingSystem
    Library             Process
    Resource            ../resource.robot
    Resource            ../keywords/BwcInventory.rst
    Resource            ../keywords/002.rst
    Variables           001_One_Switch_Inventory_Operations.yaml
    Variables           002_Verify_User_Defined_Fabric.yaml

