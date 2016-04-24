#!/usr/bin/env python
'''
Python + Ansible - Class 3 - Exercise 2
Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>

I created this program with a different concept: Data saving and load using
a yaml or json file. So the system save system resources and can be run throught
a cron or anacron job.
'''

import snmp_helper
import yaml
import json
import sys
import pygal

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



def load_saved_data(l_default):
    '''
    Load previous saved data
    '''
    try:
        with open('exercise3-2.'+file_fmt, 'r') as fhandler:
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
    return file_data


def get_snmp_data(router, snmp_user, miboid):
    '''
    Get and return snmp data
    '''
    snmp_data = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(router, snmp_user, oid=miboid))
    return snmp_data


def generate_graphic(l_data):
    '''
    Generate a SVG graphic using data passed as an argument
    '''
    graph_stats = {
        "in_octets": [],
        "out_octets": [],
        "in_ucast_pkts": [],
        "out_ucast_pkts": []
    }

    for l_label in ("in_octets", "out_octets", "in_ucast_pkts", "out_ucast_pkts"):
        l_old_value = 0
        for i in range(0, len(l_data)):
            l_value = l_data[i][l_label]
            if l_old_value == 0:
                l_diff = 0
            else:
                l_diff = int(l_value)-int(l_old_value)
            if verbose:
                print 'xxxxx: %s, diff: %s, (old: %s)' % (l_value, l_diff, l_old_value)
            graph_stats[l_label].append(l_diff)
            l_old_value = l_value
    if verbose:
        print graph_stats
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output bytes and Unicast'
    line_chart.add('InBytes', graph_stats['in_octets'])
    line_chart.add('OutBytes', graph_stats['out_octets'])
    line_chart.add('InUnicast', graph_stats['in_ucast_pkts'])
    line_chart.add('OutUnicast', graph_stats['out_ucast_pkts'])
    line_chart.render_to_file('exercise2.svg')


def main():
    '''
    Main Function
    '''
    snmp_user = (my_user, my_pass, my_enckey)
    if_ifdescr = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.2.5')
    if_in_octets = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.10.5')
    if_out_octets = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.16.5')
    if_in_ucast_pkts = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.11.5')
    if_out_ucast_pkts = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.2.2.1.17.5')
    print 'Using file format: %s' % (file_fmt)

    old_data_list = load_saved_data(0)
    # pylint: disable=maybe-no-member
    if old_data_list == 0:
        old_if_ifdescr = if_ifdescr
        old_if_in_octets = if_in_octets
        old_if_out_octets = if_out_octets
        old_if_in_ucast_pkts = if_in_ucast_pkts
        old_if_out_ucast_pkts = if_out_ucast_pkts
        data_list = range(0)
    else:
        old_if_ifdescr = old_data_list[-1]['ifdescr']
        old_if_in_octets = old_data_list[-1]['in_octets']
        old_if_out_octets = old_data_list[-1]['out_octets']
        old_if_in_ucast_pkts = old_data_list[-1]['in_ucast_pkts']
        old_if_out_ucast_pkts = old_data_list[-1]['out_ucast_pkts']
        data_list = old_data_list

    if verbose:
        print 'IfDescr: %s (last: %s)' % (if_ifdescr, old_if_ifdescr)
        print 'InOctets %s (last: %s)' % (if_in_octets, old_if_in_octets)
        print 'OutOctets %s (last: %s)' % (if_out_octets, old_if_out_octets)
        print 'In Ucast %s (last: %s)' % (if_in_ucast_pkts, old_if_in_ucast_pkts)
        print 'Out Ucast %s (last: %s)' % (if_out_ucast_pkts, old_if_out_ucast_pkts)


    # Array preparation to save data
    data_list.append({})
    data_list[-1]['ifdescr'] = if_ifdescr
    data_list[-1]['in_octets'] = if_in_octets
    data_list[-1]['out_octets'] = if_out_octets
    data_list[-1]['in_ucast_pkts'] = if_in_ucast_pkts
    data_list[-1]['out_ucast_pkts'] = if_out_ucast_pkts

    save_data(data_list)

    generate_graphic(data_list)
    if verbose:
        print '----------------------------'

if __name__ == "__main__":
    main()

quit()


