#!/usr/bin/env python
''' Exercise 6 - PyNet Python '''

import yaml
import json

my_list=range(3)
my_list.append({ 'name' : 'my_hostname', 'ip_addr' : '192.168.0.1'})

# As I run on a Unix variant, /tmp follow the FHS2 standard and is a right place to 
# create and possible forgot about temporary files 

with open("/tmp/Exercise6.yaml", "w") as file:
  file.write(yaml.dump(my_list, default_flow_style=False))
  
with open("/tmp/Exercise6.json", "w") as file:
  json.dump(my_list, file)

exit