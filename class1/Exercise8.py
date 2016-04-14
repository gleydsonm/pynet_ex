#!/usr/bin/env python
''' Exercise 8 - PyNet Python '''

from ciscoconfparse import CiscoConfParse
my_cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
var1 = my_cisco_cfg.find_objects(r"^crypto map CRYPTO")

for item in var1:
    print item.text
    for children in item.children:
	print children.text
    print '-----------------------'

