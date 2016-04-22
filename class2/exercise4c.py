#!/usr/bin/env python
'''
Exercise 4c - as also solve exercise 4b (module snmp_helper) import
I chose to use list to inform parameters and split to distribute them
among variables. That make easy to convert the program to be command line 
driven

The separator is '|', so we can handle IPV6 addresses and is more easy to
see than CSV separator ','
'''
from snmp_helper import snmp_get_oid,snmp_extract
ROUTERS=[]
ROUTERS.append('50.76.53.27|7961|galileo')
ROUTERS.append('50.76.53.27|8061|galileo')

def snmp_print_sysname(IP, PORT='161', COMMUNITY='public'):
    conn_dev = (IP, COMMUNITY, PORT)
    snmp_data = snmp_extract(snmp_get_oid(conn_dev, oid='1.3.6.1.2.1.1.5.0'))
    return snmp_data

def snmp_print_sysdescr(IP, PORT='161', COMMUNITY='public'):
    conn_dev = (IP, COMMUNITY, PORT)
    snmp_data = snmp_extract(snmp_get_oid(conn_dev, oid='1.3.6.1.2.1.1.1.0'))
    return snmp_data
    

def main():
  for ROUTER in ROUTERS:
    IP=ROUTER.split('|')[0]
    PORT=ROUTER.split('|')[1]
    COMMUNITY=ROUTER.split('|')[2]
    print "\n\n"
    print IP + ' ' + PORT + ' '+ COMMUNITY + '\n'
    output=snmp_print_sysname(IP, PORT, COMMUNITY)
    print output
    output=snmp_print_sysdescr(IP, PORT, COMMUNITY)
    print output
    print '-------------------------------------------------------------'

if __name__ == "__main__":
    main()

quit()

