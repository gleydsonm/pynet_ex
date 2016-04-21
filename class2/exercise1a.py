#!/usr/bin/env python
# Exercise 1a - Class 2 - Check module loading
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

print 'All modules sucessfully loaded. Doing something useful after this'

