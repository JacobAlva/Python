''' Decorator
    A decorator is a function that take another function as argument and extends the behaviour of the function without completely modifying it, thus allowing you to add new functionalities to the existing function.

    There are two diff decorators, function and plus decorators.
'''

import functools
"""
''' # function decorators
    Functions in Python are class objects. This means that, like any other object, they can be defined inside another function, passed as an argument to other functions or returned from a function.
'''


def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)

# the above statement can be replaced with a decorator

print_name()


def start_end_decorator1(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator1
def add5(x):
    #print(5)
    return x + 5
    
result = add5(10)
print(result)


# function identitiles
print(help(add5))
print(add5.__name__)
# the results show that Python is confused about the real identity of this fxn
# to fix that, import and use the functions

''' Template
    # This could be used as a decorator template for any function.

    def my_decorator1(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something...
        result = func(*args, **kwargs)
        # Do something...
        return result
    return wrapper
'''

"""

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet('Jacob')