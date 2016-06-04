#!/usr/bin/env python
'''
Exercise 1a - Class 8 - Foreign key association with database fields i
Gleydson Mazioli <gleydsonmazioli@gmail.com>
'''

from net_system.models import NetworkDevice, Credentials

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
    net_devices = NetworkDevice.objects.all()
    credentials = Credentials.objects.all()

    for device in net_devices:
        if 'arista' in device.device_type:
            print 'Arista'
            creds = get_cred_type(credentials, 'arista')
        elif 'cisco_ios' in device.device_type:
            print 'Standard'
            creds = get_cred_type(credentials, 'standard')
        elif 'juniper' in device.device_type:
            print 'Juniper'
            creds = get_cred_type(credentials, 'standard')
        else:
            print 'Unknown device: %s' % (device.device_type)

        print 'Associating %s with credential %s' % (device, creds.username)
        device.credentials = creds
        device.save()

if __name__ == '__main__':
    main()

