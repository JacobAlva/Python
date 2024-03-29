''' Decorator
    A decorator is a function that take another function as argument and extends the behaviour of the function without completely modifying it, thus allowing you to add new functionalities to the existing function.

    There are two diff decorators, function and plus decorators.
'''

import functools
from typing import Any
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
    def wrapper(*args, **kwargs):   # kwargs = key word arguments
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


# decorators with arguments
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


# Nexted decorators or Multiple Decorators
def startend_dec(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
@startend_dec
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')

"""


# Class Decorators
# they are used if you want to maintain and update a state

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'The function "{self.func.__name__}" has been executed {self.num_calls} times')
        return self.func(*args, **kwargs)
    
@CountCalls
def say_hello():
    print('Hello')

@CountCalls
def addOne():
    print(1+1)

say_hello()
say_hello()
say_hello()
addOne()
addOne()


''' # Decorator Use cases
    Timer decorator - calculate execution time of a function
    Debug decorator - print more info about code fxn and its arguments
    Check decorator - check if args meet some requirments and if they behave accordingly
    ---
    Register functions like plugins with decorators
    Cache the return values
    Generate information and update the state of a function
'''


''' # Understanding *args and **kwargs
    *args and **kwargs are ways to handle variable numbers of arguments in Python functions:

    *args (stands for "arguments"):
    Allows a function to accept any number of positional arguments.
    Inside the function, args is a tuple containing all the passed positional arguments.
    **kwargs (stands for "keyword arguments"):

    **kwargs (keyword arguments)
    Allows a function to accept any number of keyword arguments.
    Inside the function, kwargs is a dictionary containing all the passed keyword arguments.
    These are especially useful in decorators and other functions where you want to create flexible interfaces that work with a variety of input arguments.

    Here’s an example to illustrate both: 
'''
def example_func(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_func(1, 2, 3, a="hello", b="world")

'''
    In this example, 1, 2, 3 are captured by *args as a tuple (1, 2, 3), and a="hello", b="world" are captured by **kwargs as a dictionary {'a': 'hello', 'b': 'world'}.
'''