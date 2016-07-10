#!/usr/bin/env python
'''
Exercise 4 - class 10
'''
from jnpr.junos import Device
from jnpr.junos import exception
from jnpr.junos.utils.config import Config
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


def set_hostname(hdl, myhostname, lfmt):
    '''
    Set the hostname
    '''
    if lfmt == 'set':
        return hdl.load("set system host-name "+myhostname, format="set", merge=True)
    if lfmt == 'text':
        return hdl.load(path=myhostname, format="text", merge=True)
    if lfmt == 'xml':
        return hdl.load(path=myhostname, format="xml", merge=True)


def main():
    '''
    Main function
    '''
    a_device = remote_conn(HOST, USER, PWD)
    if not a_device:
        sys.exit('Fix the above errors. Exiting...')

    print a_device.facts
    cfg = Config(a_device)
    cfg.lock()

    print 'Set hostname using set format'
    set_hostname(cfg, 'pytest-gmaz', 'set')
    print 'Show differences'
    print cfg.diff()
    print 'Rollback'
    cfg.rollback(0)
    print 'Check if rollback is ok'
    print cfg.diff()

    print 'Set hostname using cfg file'
    set_hostname(cfg, 'hostname.conf', 'text')
    print 'Show differences'
    print cfg.diff()
    print 'Commit'
    cfg.commit(comment='Text hostname commit by gmazioli')

    print 'Set hostname using external XML'
    set_hostname(cfg, 'hostname.xml', 'xml')
    print 'Show differences'
    print cfg.diff()
    print 'Commit'
    cfg.commit(comment='XML hostname commit by gmazioli')


    print 'Reverting changes and doing the final commit'
    set_hostname(cfg, 'pynet-jnpr-srx1', 'set')
    cfg.commit(comment='System commit by gmazioli')
    cfg.unlock()

if __name__ == '__main__':
    main()

