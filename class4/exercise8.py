#!/usr/bin/env python
'''
Exercise 8 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com
'''

import netmiko

def remote_connect(host):
    '''
    Connect to the remote host
    '''
    return netmiko.ConnectHandler(**host)

def send_command(conn, cmd):
    '''
    Send a command to the remote host
    '''
    return conn.send_command(cmd)

def run_config_command_file(conn, lfile):
    '''
    Run a command in config mode
    '''
    return conn.send_config_from_file(config_file=lfile)



def main():
    '''
    Main function
    '''
    pynet1 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 8022,
    }

    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': '8022'
    }

    for rtr in  ['pynet1', 'pynet2']:
        my_rtr = remote_connect(eval(rtr))
        print 'Running commands on {}'.format(rtr)
        print run_config_command_file(my_rtr, 'exercise8.cmd')
        print my_rtr.send_command("show run | inc logging buffered")
        print '\n'

    my_rtr.disconnect()

if __name__ == "__main__":
    main()

