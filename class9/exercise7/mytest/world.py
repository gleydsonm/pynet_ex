#!/usr/bin/env python
'''
Class 9 - Exercise 7
'''

#pylint: disable=invalid-name

def func1(param='World'):
    '''
    Print a parameter when a function is called
    '''
    print param


class MyClass(object):
    '''
    MyClass - main class of exercise 7
    '''
    def __init__(self, x='param1', y='param2', z='param3'):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        '''
        Hello method
        '''
        return 'Hello: {} {}'.format(self.x, self.z)

    def not_hello(self):
        '''
        Not Hello method
        '''
        return 'Not Hello: {} {}'.format(self.y, self.z)

class MyChildClass(MyClass):
    '''
    MyChildClass
    '''
    def __init__(self, x='param1', y='param2', z='param3'):
        self.x = x
        self.y = y
        self.z = z + ' (thats all folks)'
        MyClass.__init__(self, x, y, z)

    def hello(self):
        '''
        Hello overwride method of MyChildClass
        '''
        return 'ChildClass: {} {}'.format(self.x, self.z)

if __name__ == '__main__':
    print 'world is just a module, you need to import it'
