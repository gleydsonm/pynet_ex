#!/usr/bin/env python
'''
Python + Ansible - Class 3 - Exercise 1
Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>
'''

import snmp_helper
import yaml
import json
import sys
import smtplib
from email.mime.text import MIMEText
import socket

# pylint: disable=C0103
# pylint: disable=line-too-long

my_ip = '50.76.53.27'
my_user = 'pysnmp'
my_pass = 'galileo1'
my_enckey = 'galileo1'
# pynet_rtr1 = (my_ip, 7961)
my_host = (my_ip, 8061)
verbose = True
mail_sender = 'gmazioli@localhost'
# More than one recipient can be specified here
mail_recipient = 'gmazioli'
smtp_host = 'localhost'
# File format should be json or yaml
file_fmt = 'json'


def mail_send(subject, message):
    '''
    Send a mail
    '''
    for l_recipient in mail_recipient.split(' '):
        if verbose:
            print 'Sending mail to %s' % (l_recipient)
        message = MIMEText(message)
        message['Subject'] = subject
        message['From'] = mail_sender
        message['To'] = l_recipient

        #if True:
        try:
            smtp_conn = smtplib.SMTP(smtp_host)
        except socket.gaierror:
            print 'Could not connect to remote host'
            sys.exit(1)

        # Send the email
        # pylint: disable=undefined-variable
        try:
            smtp_conn.sendmail(mail_sender, l_recipient, message.as_string())
            if verbose:
                print 'Mail to %s sent' % (l_recipient)
        except SMTPSenderRefused:
            print 'You should specify a correct sender like user@domain'
        except SMTPRecipientsRefused:
            print 'You should specify a correct recipient like user@domain'


def save_data(l_var):
    '''
    Save data
    '''
    try:
        with open('exercise3-1.'+file_fmt, 'w') as fhandler:
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
        with open('exercise3-1.'+file_fmt, 'r') as fhandler:
            if file_fmt == 'yaml':
                file_data = yaml.load(fhandler)
            elif file_fmt == 'json':
                file_data = json.load(fhandler)
            else:
                sys.exit('File Read: Invalid file format: '+file_fmt)
    except IOError:
        if verbose:
            print 'File not found: exercise3-1.'+file_fmt
        return l_default
    return file_data[0][l_var]


def get_snmp_data(router, snmp_user, miboid):
    '''
    Get and return snmp data
    '''
    snmp_data = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(router, snmp_user, oid=miboid))
    return snmp_data


def compare_values(mibname, val1, val2):
    '''
    Compare values
    '''
    l_host = my_host[0]
    if val1 != val2:
        if verbose:
            print '%s: Values differ! Old: %s  New: %s' % (mibname, val1, val2)
            mail_send('Alert: Configuration change in router', 'Hey, The configuration on router' + l_host + ' has been changed from ' + val1 + ' to ' + val2)


def main():
    '''
    Main Function
    '''

    snmp_user = (my_user, my_pass, my_enckey)
    sys_uptime = get_snmp_data(my_host, snmp_user, '1.3.6.1.2.1.1.3.0')
    running_last_changed = get_snmp_data(my_host, snmp_user, '1.3.6.1.4.1.9.9.43.1.1.1.0')
    running_last_saved = get_snmp_data(my_host, snmp_user, '1.3.6.1.4.1.9.9.43.1.1.2.0')
    startup_last_saved = get_snmp_data(my_host, snmp_user, '1.3.6.1.4.1.9.9.43.1.1.3.0')
    print 'Using file format: %s' % (file_fmt)

    old_sys_uptime = load_saved_data('sys_uptime', sys_uptime)
    old_running_last_changed = load_saved_data('run_last_changed', running_last_changed)
    old_running_last_saved = load_saved_data('run_last_saved', running_last_saved)
    old_startup_last_saved = load_saved_data('start_last_saved', startup_last_saved)

    if verbose:
        print 'Uptime: %s (last: %s)' % (sys_uptime, old_sys_uptime)
        print 'Run Last Changed: %s (last: %s)' % (running_last_changed, old_running_last_changed)
        print 'Run Last Saved: %s (last: %s)' % (running_last_saved, old_running_last_saved)
        print 'Start Lst Saved: %s (last: %s)' % (startup_last_saved, old_startup_last_saved)

    compare_values('Last Changed', old_running_last_changed, running_last_changed)

    # Array preparation to save data
    data_list = range(0)
    data_list.append({})
    data_list[0]['sys_uptime'] = sys_uptime
    data_list[0]['run_last_changed'] = running_last_changed
    data_list[0]['run_last_saved'] = running_last_saved
    data_list[0]['start_last_saved'] = startup_last_saved

    save_data(data_list)

    print '----------------------------'

if __name__ == "__main__":
    main()

quit()


