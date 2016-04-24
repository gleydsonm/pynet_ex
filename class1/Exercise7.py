#!/usr/bin/env python
''' Class 1 - Exercise 7 - PyNet + Ansible
It will just read compatible JSON and YAML files created on /tmp directory, and
after that show them using list format
'''

import yaml
import json
import pprint

# As I run on a Unix variant, /tmp follow the FHS2 standard and is a
# right place to create and possible forgot about temporary files

def main():
    '''
    Main function
    '''
    print 'The output of the loaded YAML file, is\n'
    with open("/tmp/Exercise6.yaml") as fhandler:
        new_list = yaml.load(fhandler)
        pprint.pprint(new_list)

    print '\n---------\n'

    print 'The output of the loaded JSON file, is\n'
    with open("/tmp/Exercise6.json") as fhandler:
        new_list = json.load(fhandler)
        pprint.pprint(new_list)

if __name__ == "__main__":
    main()

