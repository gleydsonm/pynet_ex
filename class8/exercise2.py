#!/usr/bin/env python
'''
Exercise 2 - Class 8 - Set vendor field
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice

def set_vendor(l_dev, l_vendor):
    '''
    Set the vendor field on the device
    '''
    # Deal first with None type return (when nothing is found on the database)
    if l_dev.vendor is None:
        print 'Setting up to vendor of %s to \'%s\'' % (l_dev, l_vendor)
    elif l_vendor not in l_dev.vendor:
        print 'Setting up to vendor of %s to \'%s\'' % (l_dev, l_vendor)
    else:
        print '%s: Vendor already set to \'%s\'' % (l_dev, l_vendor)
        return 1
    l_dev.vendor = l_vendor
    l_dev.save()


def main():
    '''
    Main function
    '''
    net_devices = NetworkDevice.objects.all()
    for device in net_devices:
        if 'arista' in device.device_type:
            print 'Arista'
            set_vendor(device, 'Arista')
        elif 'cisco_ios' in device.device_type:
            print 'Standard'
            set_vendor(device, 'Cisco IOS')
        elif 'juniper' in device.device_type:
            print 'Juniper'
            set_vendor(device, 'Juniper')
        else:
            print 'Unknown device: %s' % (device.device_type)

if __name__ == '__main__':
    main()


