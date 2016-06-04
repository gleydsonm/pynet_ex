#!/usr/bin/env python
'''
Exercise 7 - Class 8 - Thread connection to each device and run the command
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice
import netmiko
import django
import time
import threading

def get_cred_type(l_credentials, l_type):
    '''
    Get the associated credential from the database (instead
     of using a hard coded list)
    '''
    for cred in l_credentials:
        if l_type in cred.description.lower():
            return cred


def run_command(device):
    '''
    Connect and run a command on the remote host
    '''
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
        return 1

    print device, device_type, port, ip_addr, username, password
    try:
        rem_conn = netmiko.ConnectHandler(device_type=device_type, ip=ip_addr,
                                          username=username, password=password,
                                          port=port, secret=secret)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print "  %s: Unable to connect (check user/pw)" % (device)
        return 1
    print rem_conn.send_command_expect("show version")
    end_dev_time = int(time.time())
    print '*' * 70
    print 'Elapsed time on %s: %s s' % (device, end_dev_time - start_dev_time)
    print '*' * 70
    print '\n'

def main():
    '''
    Main function
    '''
    django.setup()
    net_devices = NetworkDevice.objects.all()
    start_time = int(time.time())

    for device in net_devices:
        my_thread = threading.Thread(target=run_command, args=(device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    end_time = int(time.time())
    print '\n'
    print 'Total processing time: %s seconds' % (end_time - start_time)

if __name__ == '__main__':
    main()


