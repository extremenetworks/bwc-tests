.. code:: robotframework

    *** Test Cases ***
    Check Empty BWC List
        ${result}=    Inventory List  ${FABRIC NAME}  ${FALSE}
        Should Not Contain   ${result.stdout}   Fabric
          
    Register Switch in BWC server
        ${result}=    Inventory Register  ${FABRIC NAME}  ${IP ADDRESS}  ${USER}  ${PASSWD}
        Inventory Should Contain  ${result}

    Update Switch in BWC server
        ${result}=    Inventory Update  ${FALSE}  ${IP ADDRESS}  ${USER}  ${PASSWD}
        Inventory Should Contain  ${result}

    Check BWC List with one registered switch
        ${result}=    Inventory List  ${FABRIC NAME}  ${FALSE}
        Inventory Should Contain  ${result}

    Delete Switch from BWC server
        ${result}=  Inventory Delete  ${IP ADDRESS}
        Inventory Should Contain  ${result}

    Check Empty BWC List Again
        ${result}=    Inventory List  ${FABRIC NAME}  ${FALSE}
        Should Not Contain   ${result.stdout}   Fabric

    *** Settings ***
    Resource            keywords/BwcInventory.rst
    Variables           001_One_Switch_Inventory_Operations.yaml
    Resource            resource.robot
    Suite Setup         resource.Clean Switches
    # Suite Teardown      Clean Switches
