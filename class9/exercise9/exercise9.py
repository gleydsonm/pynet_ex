#!/usr/bin/env python
'''
Class 9 - Exercise 9b

Kirk Byers: I need your feedback about external variables and pylint. I tried to solve the 
errors, but as pylint just track python variables, I dont figure if is possible to fix the 
warnings.

Tks
'''

import os
import sys
from pprint import pprint

# Set a relative structure pointing to the mytest modules
# from class 8. As I'm using the PWD to control that, It
# will be compatible with my local machine or lab environment
# without changes (reusable code)

MYHOME = os.environ['PWD']
MYHOME += '/../exercise8'
sys.path.append(MYHOME)
pprint(sys.path)

# Importing mytest from class 8 (another directory on a
# upper level structure)
from mytest import *

def main():
    '''
    Main Function
    '''
    # Show return from func1, func2 and func3 (exercise 9a)
    print 'Func1'
    func1()
    print 'Func2'
    func2()
    print 'Func3'
    func3()

    # Show hello and not_hello return (exercise 9b)
    obj1 = MyClass('Hello', 'Not Hello', 'World')
    print obj1.hello()
    print obj1.not_hello()

if __name__ == '__main__':
    main()