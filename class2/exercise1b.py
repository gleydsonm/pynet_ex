#!/usr/bin/env python
# Exercise 1b - Class 2 - Check versions
# Changes to use exceptions to check if module exist. So this could be used to
# make the programa compatible with more than one specific module if the
# preferred one isn't found on the system (like pysnmp and netsnmp)
# 
# Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>

try:
    import pysnmp
except ImportError:
     print 'pysnmp module not installed. Please install it using your package manager or PIP.'
     quit()

try:
    import paramiko
except ImportError:
     print 'paramiko module not installed. Please install it using your package manager or PIP.'
     quit()

v_pysnmp = pysnmp.__version__
v_paramiko = paramiko.__version__

print 'The pysnmp installed version is ' + v_pysnmp
print 'The paramiko installed version is ' + v_paramiko
quit()


