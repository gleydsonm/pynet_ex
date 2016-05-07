#!/usr/bin/env python
'''
Exercise 5 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com
'''

import netmiko

def remote_connect(host):
    '''
    Connect to the remote host
    '''
    return netmiko.ConnectHandler(**host)

def run_command(conn, cmd):
    '''
    Run a command
    '''
    return conn.send_command(cmd)


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
    juniper_srx = {
        'device_type': 'juniper',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 9822,
    }

    for rtr in  ['pynet1', 'pynet2', 'juniper_srx']:
        my_rtr = remote_connect(eval(rtr))
        print 'Running commands on {}'.format(rtr)
        print my_rtr.send_command("show arp")
        print '\n'

    my_rtr.disconnect()


if __name__ == "__main__":
    main()
