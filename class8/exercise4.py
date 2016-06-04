#!/usr/bin/env python
'''
Exercise 4 - Class 8 - Delete device8 and device9 from the database
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice
import django

def delete_device(l_name):
    '''
    Delete a Network device
    '''
    try:
        d_dev = NetworkDevice.objects.get(device_name=l_name)
        d_dev.delete()
        print 'Deleting object %s' % (l_name)
    except NetworkDevice.DoesNotExist:
        print 'Object %s not found on the database' % (l_name)


def main():
    '''
    Main function
    '''
    django.setup()
    delete_devices = ['device8', 'device9']

    for delete_dev in delete_devices:
        delete_device(delete_dev)

if __name__ == '__main__':
    main()


