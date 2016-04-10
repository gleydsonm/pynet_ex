#!/usr/bin/env python
''' Exercise 7 - PyNet Python 
It will just read compatible JSON and YAML files created on /tmp directory, and
after that show them using list format
'''

import yaml
import json
import pprint

# As I run on a Unix variant, /tmp follow the FHS2 standard and is a right place to 
# create and possible forgot about temporary files 

print 'The output of the loaded YAML file, is\n'
with open("/tmp/Exercise6.yaml") as file:
  new_list = yaml.load(file)
  pprint.pprint(new_list)

print '\n---------\n'
  
print 'The output of the loaded JSON file, is\n'
with open("/tmp/Exercise6.json") as file:
  new_list=json.load(file)
  pprint.pprint(new_list)

exit
