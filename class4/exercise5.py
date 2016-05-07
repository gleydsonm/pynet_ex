#!/usr/bin/env python
'''
Exercise 5 - Class 4
Gleydson Mazioli <gleydsonmazioli@gmail.com
'''

import netmiko

def remote_connect(host):
    '''
    Conect to the remote host
    '''
    return netmiko.ConnectHandler(**host)

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
    my_rtr = remote_connect(pynet2)
    print 'Running commands on %s' % (my_rtr.ip)
    my_rtr.find_prompt()
    my_rtr.config_mode()
    if my_rtr.config_mode():
        print ' roteador %s em config mode' % (my_rtr.ip)
    else:
        print ' roteador %s fora do config mode' % (my_rtr.ip)

    out = my_rtr.send_command("show version")
    print out

    my_rtr.disconnect()


if __name__ == "__main__":
    main()
