#!/usr/bin/env python
# Exercise 1c - Class 2 - Try to import my_func in current directory,
#              if not found, try the modules directory. As last resource
#               try the modules package of home dir ~/applied_python/lib/python2.7/site-packages/
#               I chose to use sys and os modules instead of PYTHONPATH here, to keep most
#               stuff under the control of Python

# Gleydson Mazioli da Silva <gleydsonmazioli@gmail.com>

try:
    import os
except ImportError:
    print 'Hmm, if I cant find the os module, something is very strange...'
    quit()

try:
    import sys
except ImportError:
    print 'Hmm, if I cant find the sys module, something is very strange...'
    quit()


# First try: Import from current directory
try:
    from my_func import my_func
    print 'Found my_func in current directory'
except ImportError:
    # Second try: Import from the modules directory
    try:
        # subdirectory separator is '.' instead of '/' here. 
        # We are using relative path
        # __init__.py is needed in such import and work as a helper
        # to python
        from modules.my_func import my_func
        print 'Found my_func in modules subdiretory'
    except:
        try:
            myhome=os.environ['HOME']
            myhome+='/applied_python/lib/python2.7/site-packages/'
            sys.path.append(myhome)
            from my_func import my_func
            print 'Found my_func in ~/applied_python/lib/python2.7/site-packages/'
        except ImportError:
            print 'module my_func not installed. Double check your system install.'
            quit()

print 'Do something useful after that'
quit()


