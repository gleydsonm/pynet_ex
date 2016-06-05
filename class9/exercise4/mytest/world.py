#!/usr/bin/env python
'''
Class 9 - Exercise 4
'''

#pylint: disable=invalid-name

def func1(param='World'):
    '''
    Print a parameter when a function is called
    '''
    print param


class MyClass(object):
    '''
    Main Class to return Class stuff
    '''
    def __init__(self, x='param1', y='param2', z='param3'):
        '''
        Initialization of the variables
        '''
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        '''
        Hello Method. return variables x and z
        '''
        return 'Hello: {} {}'.format(self.x, self.z)

    def not_hello(self):
        '''
        not_hello method, return variables y and z
        '''
        return 'Not Hello: {} {}'.format(self.y, self.z)

if __name__ == '__main__':
    print 'world is just a module, you need to import it'
