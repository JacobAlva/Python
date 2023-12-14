"""
    Functions

    - The difference between arguments and parameters
        Parameters are variables that are defined or used inside parenthesis while defining a function, while arguments are the values passed for the parameters whiile calling a function. 
        DPCA - define(parameters)/call(arguments)
            def some_func(parameters)
            some_func(argument)

    - Positional and keyword arguments 
    - Default arguments
    - Variable-length arguments (*args and **kwargs)
    - Container unpacking into function arguments 
    - Local vs. global arguments
    - Parameter passing (by value or by reference?)
"""

"""
# Parameters & Arguments
def print_name(name):           # parameter
    print(f"Your name is {name}")

print_name('Fred')              # argument


# Positional & Keyword arguments
def clips(a, b, cc):
    print(a, b, cc)

clips(1, 2, 3)          # these are positional arguments 
# positional arguments assign the arguments to the parameters based on their position

clips(a=1, b=2, cc=3)
#clips(1, b=2, 3)        # SyntaxError - Positional argument cannot appear after keyword arguments
clips(cc=1, b=2, a=3)    # with keyword arguments, the position are not important but the keywords must be same as the parameters
clips(1, b=2, cc=3)       # TypeError - multiple values for argument 'a' as it has been used as a positional argument 


# Default arguments
def clips(a, b=2, cc, d=4):
    print(a, b, cc, d)

clips(1,2,3)        # auto joins the default value
clips(1,2,3,7)      # the default value can be overwritten at the point of call.
    

def clipa(a, b=2, cc, d=4):          # default values can only be used at the end of the declaration. non-default argument cannot follow default argument.
    print(a, b, cc, d)
"""

# Variable length arguments
"""
'''
    if you mark a parameter with '*', you can pass any number of positional arguments to your function 
    and ** allows you to pass any number of keyword arguments to the function. 
    They are typically called *args and **kwargs but can be called anything
    The *args is a tuple while the **kwargs is a dictionary
'''
def varle(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    #for keey in kwargs:
    #    print(keey, kwargs[keey])
    for key, val in kwargs.items():
        print(key,":", val)

#varle(1, 2, 3, 4, 5, six = 6, sev = 7)
varle(1, 2, six = 6, sev = 7)               # You can skip any of the variable length arguments
#varle(1, 2, 3, six=4, 5)                     # positional argument can't follow keyword argument
"""

# Forcing  keyword argument
"""
''' By using a *, it ensures that a max of two positional arguments are used, while the rest are keyword arguments'''
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, d=3, c=4)

def forand(*args, last):
    for arg in args:
        print(arg)
    print(last)
forand(3, 5, last= 4)

# you can pass an empty argument to a variable length only function
def forand(*args):
    for arg in args:
        print(arg)
forand()
"""