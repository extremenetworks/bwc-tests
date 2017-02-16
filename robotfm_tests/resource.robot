*** Keywords ***
Clean Switches
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Log To console   Suite setup and Teardown: Cleaning Switches!!!
      ${result}=       Run Process   python          setup_teardown/VDX_clean_fabric.py   -f   setup_teardown/VDX_clean_fabric_IP.txt
      Log To Console   Return Code: ${result.rc}
      # Uncomment the following lines it Return code is not 0
      Log To Console   all output:\n ${result.stdout}
      # Log To Console   err: ${result.stderr}
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clean NOSSwitch
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Log To console   Suite setup and Teardown: Cleaning Switches!!!
      ${result}=       Run Process   python         setup_teardown/NOS_clean_fabric.py   -f   setup_teardown/NOS_clean_IP.txt
      Log To Console   Return Code: ${result.rc}
      # Uncomment the following lines it Return code is not 0
      Log To Console   all output:\n ${result.stdout}
      # Log To Console   err: ${result.stderr}
      Log To console   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*** Settings ***
Library             Process
