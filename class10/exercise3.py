#!/usr/bin/env python
'''
Exercise 3 - class 10
'''
from jnpr.junos import Device
from jnpr.junos import exception
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
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

    route_table = RouteTable(a_device)
    route_table.get()
    for route in route_table.keys():
        print route
        route_items = dict(route_table[route].items())
        print '   Oper: %s' % (route_items['nexthop'])
        print '   rx: %s' % (route_items['age'])
        print '   tx: %s' % (route_items['via'])
        print '   prot: %s' % (route_items['protocol'])
        print

if __name__ == '__main__':
    main()

