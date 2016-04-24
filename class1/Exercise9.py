#!/usr/bin/env python
''' Exercise 9 - PyNet Python '''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Main function
    '''
    my_cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    out = my_cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO', childspec=r'set pfs group 2')
    for item in out:
        print item.text

if __name__ == "__main__":
    main()


