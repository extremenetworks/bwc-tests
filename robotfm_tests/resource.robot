*** Keywords ***
Clean Switches
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Log To console   Suite setup and Teardown: Cleaning Switches!!!
      ${result}=       Run Process   python          setup_teardown/clean_fabric.py   -f   setup_teardown/clean_fabric_IP.txt
      Log To Console   Return Code: ${result.rc}
      # Uncomment the following lines it Return code is not 0
      Log To Console   all output:\n ${result.stdout}
      # Log To Console   err: ${result.stderr}
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clean NOSSwitch_Network_Essentials
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Log To console   Suite setup and Teardown: Cleaning Switches!!!
      ${result}=       Run Process   python         setup_teardown/NOS_clean_fabric.py   -f   003_NOS_Network_Essentials
      Log To Console   Return Code: ${result.rc}
      # Uncomment the following lines it Return code is not 0
      Log To Console   all output:\n ${result.stdout}
      # Log To Console   err: ${result.stderr}
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Clean NOSSwitch_Virtual_Fabric
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Log To console   Suite setup and Teardown: Cleaning Switches!!!
      ${result}=       Run Process   python         setup_teardown/NOS_clean_fabric.py   -f   004_NOS_Virtual_Fabric
      Log To Console   Return Code: ${result.rc}
      # Uncomment the following lines it Return code is not 0
      Log To Console   all output:\n ${result.stdout}
      # Log To Console   err: ${result.stderr}
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






*** Settings ***
Library             Process
