#!/usr/bin/env python
'''
Exercise 2 - Class 7
Using pyeapi to obtain the fields inOctets and outOcters for each
interface on the swtch.
'''
import pyeapi
import sys
import argparse

def check_vlan_exist(l_conn, vlan_id):
    '''
    Check if a vlan already exist
    '''
    cmd = 'show vlan id %s' % (vlan_id)
    try:
        ret = l_conn.enable(cmd)
        vlan_list = ret[0]['result']
        if vlan_list['vlans'][str(vlan_id)]:
            return True
    except pyeapi.eapilib.CommandError:
        return False
    return False


def main():
    '''
    Main Loop
    '''
    parser = argparse.ArgumentParser(description='Test of argparse')
    parser.add_argument('--add', action="store", dest="add", help="Add a Vlan with color ex: --add 100")
    parser.add_argument('--color', action="store", dest="color", help="Sepecify a VLAN description, ex: --color BLUE")
    parser.add_argument('--rem', action="store", dest="rem", help="Remove a VLAN, ex: --rem 100")
    parser.add_argument('--version', action='version', version='%(prog)s 0.01')
    parseresults = parser.parse_args()
    if parseresults.add and parseresults.rem:
        sys.exit('You should not specify --add and --rem at the same time')
    if parseresults.add and not parseresults.color:
        sys.exit('When using --add, you also need to specify the --color argument')

    try:
        sw_conn = pyeapi.connect_to(SWITCH)
    except AttributeError:
        sys.exit('Unable to connect to the remote switch')
    commands = []
    if parseresults.add:
        if not check_vlan_exist(sw_conn, parseresults.add):
            commands = ['vlan '+parseresults.add, 'name '+parseresults.color]
        else:
            print 'Vlan %s is already configured on %s' % (parseresults.add, SWITCH)
    if parseresults.rem:
        if check_vlan_exist(sw_conn, parseresults.rem):
            commands = ['no vlan '+parseresults.rem]
        else:
            print 'Vlan %s not found on %s' % (parseresults.rem, SWITCH)
    sw_conn.config(commands)


if __name__ == "__main__":
    SWITCH = 'pynet-sw1'
    main()

