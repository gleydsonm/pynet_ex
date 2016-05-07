#!/usr/bin/env python
'''
Exercise 5 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com
'''

import netmiko

def remote_connect(host):
    '''
    Connect to a remote host
    '''
    return netmiko.ConnectHandler(**host)

def send_command(conn, cmd):
    '''
    Send a command
    '''
    return conn.send_command(cmd)

def run_config_command(conn, cmd):
    '''
    Run a command in config mode
    '''
    return conn.send_config_set(cmd)


def main():
    '''
    Main function
    '''
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': '8022'
    }

    for rtr in  ['pynet2']:
        my_rtr = remote_connect(eval(rtr))
        config_cmds = ['logging buffered 65535']
        print 'Running commands on {}'.format(rtr)
        print run_config_command(my_rtr, config_cmds)
        print my_rtr.send_command("show run | inc logging buffered")
        print '\n'

    my_rtr.disconnect()


if __name__ == "__main__":
    main()

