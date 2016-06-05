#!/usr/bin/env python
'''
Class 9 - Exercise 5
'''
#pylint: disable=invalid-name

def func1(param='World'):
    '''
    Print a parameter when a function is called
    '''
    print param


class MyClass(object):
    '''
    Main Class of the class exercise
    '''
    def __init__(self, x='param1', y='param2', z='param3'):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        '''
        Hello method. Return x and z
        '''
        return 'Hello: {} {}'.format(self.x, self.z)

    def not_hello(self):
        '''
        Not Hello method. Return y and z
        '''
        return 'Not Hello: {} {}'.format(self.y, self.z)


class MyChildClass(MyClass):
    '''
    MyChildClass
    '''
    def hello(self):
        return 'ChildClass: {} {}'.format(self.x, self.z)


if __name__ == '__main__':
    print 'world is just a module, you need to import it'
