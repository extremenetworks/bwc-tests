#!/usr/bin/env python
import socket
import time
import traceback
from argparse import ArgumentParser

import concurrent.futures
import paramiko

EXECUTOR = concurrent.futures.ThreadPoolExecutor(50)


def connection_list(device_file):
	ip_list = []
	try:
		with open(device_file, 'r') as selected_device_file:
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
		switch_state_map[switch] = EXECUTOR.submit(clean_switches, opt)

	for k, v in switch_state_map.items():
		try:
			print "=" * 30, k, "=" * 30
			for __ in v.result():
				if 'No entries found.' in __:
					print "\nSuccessfully cleaned switch: {0}\n".format(k)
		except:
			traceback.print_exc()


def clean_switches(switch_info):
	net_connect = None
	try:
		remote_conn_pre = paramiko.SSHClient()
		# Automatically add untrusted hosts (make sure okay for security policy in
		# your environment)
		remote_conn_pre.set_missing_host_key_policy(
			paramiko.AutoAddPolicy())

		remote_conn_pre.connect(switch_info['ip'], username=switch_info['username'], password=[
			'password'], look_for_keys=False, allow_agent=False)

		# Use invoke_shell to establish an 'interactive session'
		remote_conn = remote_conn_pre.invoke_shell()
		# Strip the initial router prompt
		output = remote_conn.recv(1000)
		# Now let's try to send the router a command
		remote_conn.send("\n")
		# Open command file based on the last octet of IP
		last_octet = switch_info['ip'].split('.')[3]
		cmd_file = 'setup_teardown/Fabric_switch_configs/{0}.config'.format(last_octet)
		# print cmd_file
		try:
			# Example: for 10.24.39.245 it will use file 245.config
			with open(cmd_file, 'r') as selected_cmd_file:

				# Starting from the beginning of the file
				selected_cmd_file.seek(0)
				li = []
				# Writing each line in the file to the device
				for each_line in selected_cmd_file.readlines():
					remote_conn.send(each_line.strip('\r') + '\n')
					# Wait for the command to complete
					time.sleep(0.2)
					output = remote_conn.recv(500)
					li.append(output)
				return li
		except IOError:
			print 'Please add file for: {0} in folder ' \
				  '"switch_configs"'.format(switch_info['ip'])
	except socket.timeout as error:
		print "* Connection timed out. \n* Please check the " \
			  "the IP address: {0}!".format(switch_info['ip'])
	except paramiko.PasswordRequiredException as error:
		print error
	except paramiko.AuthenticationException:
		print "* Invalid username or password. \n* Please check the " \
			  "username/password or the device configuration!"
		print "* Closing program...\n"
	except Exception:
		print "General Exception during switch cleanup script execution"
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
