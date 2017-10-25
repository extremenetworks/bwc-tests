from netmiko import ConnectHandler
from argparse import ArgumentParser
from netmiko.ssh_exception import NetMikoTimeoutException, \
    NetMikoAuthenticationException

def executed_command(arg):
    mydevice = {
    'device_type': 'brocade_vdx',
    'ip': arg.host.strip(),
    'username': arg.user.strip(),
    'password': arg.password.strip(),
    'verbose': False
    }

    ssh_conn = ConnectHandler(**mydevice)
    command = arg.command
    print('>>> running command : ' + command)
    output = ssh_conn.send_command_expect(command)
    print('Result = ' + output + '\n')


parser = ArgumentParser(description='VDX config script')
parser.add_argument('-c', '--command', help='command')
parser.add_argument('-i', '--host', help='command')
parser.add_argument('-u', '--user', help='command')
parser.add_argument('-p', '--password', help='command')
args = parser.parse_args()
print args

try:
    executed_command(args)

except Exception as ex:
    if ex.message.__contains__('Unicode'):
        print "usage: netmiko_example.py [-h] [-f FILENAME]"
    elif ex.message.__contains__('\'NoneType\' object is not iterable'):
        print "No config file found"
    else:
        print ex.message
