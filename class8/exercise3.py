#!/usr/bin/env python
'''
Exercise 3 - Class 8 - Add 2 devices named devic8 and device9 to the database
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice, Credentials
import django

def create_device(l_dev, l_name, l_type, l_addr, l_port):
    '''
    Create a Network device on the database
    '''
    l_ret = l_dev.get_or_create(
        device_name=l_name,
        device_type=l_type,
        ip_address=l_addr,
        port=l_port
    )
    if l_ret[1] == True:
        print 'Object %s created sucessfully' % (l_name)
    else:
        print 'Object %s already exist' % (l_name)


def main():
    '''
    Main function
    '''
    django.setup()
    net_devices = NetworkDevice.objects.all()
    create_devices = [
        ['device8', 'cisco_ios', '5.6.7.8', '822'],
        ['device9', 'cisco_ios', '5.6.7.9', '822']
    ]

    for create_dev in create_devices:
        create_device(net_devices, *create_dev)

if __name__ == '__main__':
    main()


