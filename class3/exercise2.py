#!/usr/bin/env python
'''
Python + Ansible - Class 3 - Exercise 2
Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>
'''

import snmp_helper
import yaml
import json
import sys

# pylint: disable=C0103
# pylint: disable=line-too-long

my_ip = '50.76.53.27'
my_user = 'pysnmp'
my_pass = 'galileo1'
my_enckey = 'galileo1'
my_host = (my_ip, 7961)
verbose = True
# File format should be json or yaml
file_fmt = 'json'


def save_data(l_var):
    '''
    Save data
    '''
    try:
        with open('exercise3-2.'+file_fmt, 'w') as fhandler:
            if file_fmt == 'yaml':
                fhandler.write(yaml.dump(l_var, default_flow_style=False))
            elif file_fmt == 'json':
                json.dump(l_var, fhandler)
            else:
                print 'Unknown format: %s' % (file_fmt)
                sys.exit(1)
    except IOError:
        print 'An error happened: '



def load_saved_data(l_var, l_default):
    '''
    Load previous saved data
    '''
    try:
        with open('exercise2-1.'+file_fmt, 'r') as fhandler:
            if file_fmt == 'yaml':
                file_data = yaml.load(fhandler)
            elif file_fmt == 'json':
                file_data = json.load(fhandler)
            else:
                sys.exit('File Read: Invalid file format: '+file_fmt)
    except IOError:
        if verbose:
            print 'File not found: exercise3-2.'+file_fmt
        return l_default
    return file_data[0][l_var]


def get_snmp_data(router, snmp_user, miboid):
    '''
    Get and return snmp data
    '''
    snmp_data = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(router, snmp_user, oid=miboid))
    return snmp_data


def diff_values(val1, val2):
    '''
    Do the subtraction to get the delta value of time series data
    '''
    l_result = val2-val1
    # Take care of counter interfaces roll over or after a reboot
    if l_result < 0:
        l_result = val1
    return l_result


def main():
    '''
    Main Function
    '''
    snmp_user = (my_user, my_pass, my_enckey)
    if_ifdescr = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.2.5')
    if_in_octets = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.10.5')
    if_out_octets = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.16.5')
    if_in_ucast_pkts = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.11.5')
    if_out_ucast_pkts = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.17.')
    print 'Using file format: %s' % (file_fmt)

    old_if_ifdescr = load_saved_data('if_descr', if_ifdescr)
    old_if_in_octets = load_saved_data('if_in_octets', if_in_octets)
    old_if_out_octets = load_saved_data('if_out_octets', if_out_octets)
    old_if_in_ucast_pkts = load_saved_data('if_in_ucast_pkts', if_in_ucast_pkts)
    old_if_out_ucast_pkts = load_saved_data('if_out_ucast_pkts', if_out_ucast_pkts)

    if verbose:
        print 'IfDescr: %s (last: %s)' % (if_ifdescr, old_if_ifdescr)
        print 'InOctets %s (last: %s)' % (if_in_octets, old_if_in_octets)
        print 'OutOctets %s (last: %s)' % (if_out_octets, old_if_out_octets)
        print 'In Ucast %s (last: %s)' % (if_in_ucast_pkts, old_if_in_ucast_pkts)
        print 'Out Ucast %s (last: %s)' % (if_out_ucast_pkts, old_if_out_ucast_pkts)

    result = diff_values(old_if_ifdescr, if_ifdescr)
    print result

    # Array preparation to save data
    data_list = range(0)
    data_list.append({})
    data_list[0]['if_descr'] = if_ifdescr
    data_list[0]['in_octets'] = if_in_octets
    data_list[0]['out_octets'] = if_out_octets
    data_list[0]['in_ucast_pkts'] = if_in_ucast_pkts
    data_list[0]['out_ucast_pkts'] = if_out_ucast_pkts

    save_data(data_list)

    print '----------------------------'

if __name__ == "__main__":
    main()

quit()


