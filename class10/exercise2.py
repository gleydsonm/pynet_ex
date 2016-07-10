#!/usr/bin/env python
'''
Exercise 2 - class 10
'''
from jnpr.junos import Device
from jnpr.junos import exception
from jnpr.junos.op.ethport import EthPortTable
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

    ports = EthPortTable(a_device)
    ports.get()
    for port in ports.keys():
        print port
        port_items = dict(ports[port].items())
        print '   Oper: %s' % (port_items['oper'])
        print '   rx: %s' % (port_items['rx_packets'])
        print '   tx: %s' % (port_items['tx_packets'])
        print

if __name__ == '__main__':
    main()

