#!/usr/bin/env python
from netmiko import ConnectHandler
from argparse import ArgumentParser
from netmiko.ssh_exception import NetMikoTimeoutException, \
    NetMikoAuthenticationException
import concurrent.futures
import traceback

EXECUTOR = concurrent.futures.ThreadPoolExecutor(50)


def connection_list(device_file):
    ip_list = []
    try:

        file_name = 'setup_teardown/'+device_file + '_IP.txt'
        with open(file_name, 'r') as selected_device_file:
            selected_device_file.seek(0)
            # Getting each device IP and appending it in a list
            for each_ip in selected_device_file:
                ip = each_ip.rstrip('\n\r')
                ip_list.append(ip)
    except IOError:
        print 'ERROR: Please check the file name: {0}'.format(device_file)

    # print ip_list
    return ip_list


def update_switches(arg):
    switch_state_map = {}
    device_file = arg.filename
    switches = connection_list(device_file)
    for switch in switches:
        opt = {
            'device_type': 'brocade_vdx',
            'ip': switch,
            'username': "admin",
            'password': "password",
            'verbose': False
        }
        switch_state_map[switch] = EXECUTOR.submit(clean_switches, opt,device_file)

    for k, v in switch_state_map.items():
        try:
            print "=" * 30, k, "=" * 30
            for __ in v.result():
                if 'No entries found.' in __:

                    print "\nSuccessfully cleaned switch: {0}\n".format(k)
        except:
            traceback.print_exc()


def clean_switches(switch_info,device_file):
    net_connect = None
    try:
        net_connect = ConnectHandler(**switch_info)

        # Setting terminal length for entire output - no pagination
        output = net_connect.send_command('terminal length 0')
        # print output
        # time.sleep(1)

        # Entering global config mode
        net_connect.send_command('terminal length 0')
        #net_connect.config_mode()
        #better to send config command using send_config_set
        #output = net_connect.send_command('configure terminal')
        # print output
        # time.sleep(1)

        # Open command file based on the last octet of IP
        ip_string = switch_info['ip'].replace('.','_')
        cmd_file = 'setup_teardown/NOS_switch_configs/{0}_{1}.config'.format(
            device_file,ip_string)
        print cmd_file
        # print cmd_file
        try:
            with open(cmd_file, 'r') as selected_cmd_file:

                # Starting from the beginning of the file
                selected_cmd_file.seek(0)
                li = []
                """
                for each_line in selected_cmd_file.readlines():
                    print each_line
                    if not each_line.startswith('#'):
                        output = net_connect.send_command(each_line.strip(
                            '\r'))
                        li.append(output)
                    # time.sleep(.55)
                    # print li
                return li
                """
                for each_line in selected_cmd_file.readlines():
                    print each_line
                    if not each_line.startswith('#'):
                        li.append(each_line.strip('\r'))

                return [net_connect.send_config_set(li)]

        except IOError:
            print 'Please add file for: {0} in folder ' \
                  '"switch_configs"'.format(switch_info['ip'])
    except NetMikoTimeoutException:
        print "* Connection timed out. \n* Please check the " \
              "the IP address: {0}!".format(switch_info['ip'])
    except NetMikoAuthenticationException:
        print "* Invalid username or password. \n* Please check the " \
              "username/password or the device configuration!"
        print "* Closing program...\n"

    finally:
        if net_connect is not None:
            net_connect.disconnect()


parser = ArgumentParser(description='VDX config script')
parser.add_argument('-f', '--filename', help='File containing IP addresses. '
                                             'One in each line.')
args = parser.parse_args()

try:
    update_switches(args)

except Exception as ex:
    if ex.message.__contains__('Unicode'):
        print "usage: netmiko_example.py [-h] [-f FILENAME]"
    elif ex.message.__contains__('\'NoneType\' object is not iterable'):
        print "No config file found"
    else:
        print ex.message
