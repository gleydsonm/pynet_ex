#!/usr/bin/env python
''' Exercise 9 - PyNet Python '''

from ciscoconfparse import CiscoConfParse
my_cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

out = my_cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")
for item in out:
    print item.text
    out2 = my_cisco_cfg.find_objects_w_parents(parentspec=str(item.text), childspec=r"set transform-set")
    for item2 in out2:
	print item2.text

