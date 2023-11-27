'''
    A decorator is a function that take another function as argument and extends the behaviour of the function without completely modifying it, thus allowing you to add new functionalities to the existing function.

    There are two diff decorators, function and plus decorators.
'''

"""
# function decorators
'''
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

"""

def start_end_decorator1(func):
    
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

