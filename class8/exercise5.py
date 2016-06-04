#!/usr/bin/env python
'''
Exercise 5 - Class 8 - Connect to each device onthe database
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice
import netmiko
import django
import time

def get_cred_type(l_credentials, l_type):
    '''
    Get the associated credential from the database (instead of
     using a hard coded list)
    '''
    for cred in l_credentials:
        if l_type in cred.description.lower():
            return cred


def main():
    '''
    Main function
    '''
    django.setup()
    net_devices = NetworkDevice.objects.all()
    start_time = int(time.time())

    for device in net_devices:
        device_type = device.device_type
        port = device.port
        secret = ''
        ip_addr = device.ip_address
        creds = device.credentials
        start_dev_time = int(time.time())
        try:
            username = creds.username
            password = creds.password
        except AttributeError:
            print '%s: No credentials attributes for login. Skipping' % (device)
            continue

        print '*' * 70
        print device, device_type, port, ip_addr, username, password
        print '*' * 70
        try:
            rem_conn = netmiko.ConnectHandler(device_type=device_type,
                                              ip=ip_addr, username=username,
                                              password=password,
                                              port=port, secret=secret)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            print "  %s: Unable to connect (check user/pw)" % (device)
            continue
        print rem_conn.send_command_expect("show version")
        end_dev_time = int(time.time())
        print '\n'
        print 'Elapsed time %s: %s s' % (device, end_dev_time - start_dev_time)
        print '\n'

    end_time = int(time.time())
    print '\n'
    print 'Total processing time: %s seconds' % (end_time - start_time)

if __name__ == '__main__':
    main()


