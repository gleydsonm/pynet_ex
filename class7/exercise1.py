#!/usr/bin/env python
'''
Exercise 1 - Class 7
Using pyeapi to obtain the fields inOctets and outOcters for each
interface on the swtch.
'''
import pyeapi
import sys

def main():
    '''
    Main Loop
    '''
    try:
        sw_conn = pyeapi.connect_to(SWITCH)
    except AttributeError:
        sys.exit('Unable to connect to the remote switch')

    sh_ifaces = sw_conn.enable('show interfaces')
    ret_ifaces = sh_ifaces[0]['result']['interfaces']
    for iface in ret_ifaces:
        print iface
        try:
            print '    inOctets: %s' % (ret_ifaces[iface]['interfaceCounters']['inOctets'])
            print '    outOctets: %s' % (ret_ifaces[iface]['interfaceCounters']['outOctets'])
        except KeyError:
            print '    inOctets: 0'
            print '    outOctets: 0'


if __name__ == "__main__":
    SWITCH = 'pynet-sw1'
    main()

