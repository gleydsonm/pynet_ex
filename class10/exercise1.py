#!/usr/bin/env python
'''
Exercise 1 - class 10
'''
from jnpr.junos import Device
from jnpr.junos import exception
from getpass import getpass
from pprint import pprint
import sys

HOST = '184.105.247.76'
USER = 'pyclass'
PWD = getpass()

def remote_conn(hst, usr, pwd):
    '''
    Open the remote connection to the device
    '''
    try:
        dev = Device(host=hst, user=usr, password=pwd)
        o_dev = dev.open()
    except exception.ConnectAuthError:
        print 'Incorrect username or password'
        return False
    return o_dev


def main():
    '''
    Main function
    '''
    a_device = remote_conn(HOST, USER, PWD)
    if not a_device:
        sys.exit('Fix the above errors. Exiting...')

    pprint(a_device.facts)

if __name__ == '__main__':
    main()

