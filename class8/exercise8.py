#!/usr/bin/env python
'''
Exercise 8 - Class 8 - Thread connection to each device and run the command
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice
import netmiko
import django
import time
from multiprocessing import Process, Queue

def get_cred_type(l_credentials, l_type):
    '''
    Get the associated credential from the database (instead of
     using a hard coded list)
    '''
    for cred in l_credentials:
        if l_type in cred.description.lower():
            return cred


def run_command(device, queue):
    '''
    Connect to a host and run a command
    '''
    device_type = device.device_type
    port = device.port
    secret = ''
    ip_addr = device.ip_address
    creds = device.credentials
    out_dict = {}
    try:
        username = creds.username
        password = creds.password
    except AttributeError:
        print '%s: No credentials attributes for login. Skipping' % (device)
        return 1

    try:
        rem_conn = netmiko.ConnectHandler(device_type=device_type, ip=ip_addr,
                                          username=username, password=password,
                                          port=port, secret=secret)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print "  %s: Unable to connect (check user/pw)" % (device)
        return 1
    out = ('*' * 70) + '\n'
    out += rem_conn.send_command_expect("show version")
    out += ('*' * 70) + '\n'
    out_dict[device.device_name] = out
    queue.put(out_dict)


def main():
    '''
    Main function
    '''
    django.setup()
    net_devices = NetworkDevice.objects.all()
    start_time = int(time.time())
    queue = Queue(maxsize=20)
    procs = []
    for device in net_devices:
        my_proc = Process(target=run_command, args=(device, queue))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        a_proc.join()

    while not queue.empty():
        my_dict = queue.get()
        for k, value in my_dict.iteritems():
            print '*' * 70
            print k
            print value

    print '\nElapsed time: %s sec' % (int(time.time()) - start_time)

if __name__ == '__main__':
    main()


