#!/usr/bin/env python
'''
Exercise 4c - as also solve exercise 4b (module snmp_helper) import
I chose to use list to inform parameters and split to distribute them
among variables. That make easy to convert the program to be command line
driven

The separator is '|', so we can handle IPV6 addresses and is more easy to
see than CSV separator ','
'''
from snmp_helper import snmp_get_oid, snmp_extract

def snmp_print_sysname(l_ip, l_port='161', l_community='public'):
    '''
    Print snmp sysname
    '''
    conn_dev = (l_ip, l_community, l_port)
    snmp_data = snmp_extract(snmp_get_oid(conn_dev, oid='1.3.6.1.2.1.1.5.0'))
    return snmp_data

def snmp_print_sysdescr(l_ip, l_port='161', l_community='public'):
    '''
    Print snmp sysdescr
    '''
    conn_dev = (l_ip, l_community, l_port)
    snmp_data = snmp_extract(snmp_get_oid(conn_dev, oid='1.3.6.1.2.1.1.1.0'))
    return snmp_data


def main():
    '''
    Main function
    '''
    routers = [
        ('50.76.53.27|7961|galileo'),
        ('50.76.53.27|8061|galileo')
    ]

    for router in routers:
        my_ip, my_port, my_community = router
        print "\n\n"
        print '%s %s %s \n' % (my_ip, my_port, my_community)
        output = snmp_print_sysname(my_ip, my_port, my_community)
        print output
        output = snmp_print_sysdescr(my_ip, my_port, my_community)
        print output
        print '-'*50

if __name__ == "__main__":
    main()

quit()

