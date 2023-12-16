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

# Unpacking arguments
"""
''' You can unpack an iterable into a function's argument'''

def samp(a, b, c):
    print(a, b, c)

list1 = [1, 2, 3]       # the iterable must be the same length as the function's parameters
tuple1 = (3, 4, 5)
dict1 = {'a':6, 'b':7, 'c':8}       # for dicionaries, it must have the same keys as the declared parameters

samp(*list1)
samp(*tuple1)
samp(**dict1)        # use a **kwarg for dictionaries, else, it will print the keys
"""


# Local and Global variables
"""
def samp1():
    # opA
    # x = number
    # number = 3      # this will raise an UnboundLocalError as the program attempts to reference a local variable before assignment above.
    
    #opB
    # instead, use a global variable to retain/modify the value of number globally
    global number
    x = number      # refenrences the external global variable
    number = 3      # assigns the value of three to the global variable now.
    
    print('number inside function:', x)

number = 0
samp1()
print(number)   # returns 3 as the global value of 'number'


def samp2():
    # opA
    #number = 3      # this is a local variable and doesn't affect the global value of number.

    # opB
    # to modify the global value, you will use the 'global' keyword to reference the global variable
    global number
    number = 5
    print('num inside fxn:', number)

number = 0      # this becomes useless in opB
samp2()
print('global num:', number)
"""

# Parameter passing | Dealing with mutable and immutable objects
# mutable objects can be modified within a function while immutable objects cannot, they can rather be changed/reassigned
# immutable objects within a mutable object can be changed

def samp3(x):
    x = 4     # creates a local variable 
    print(x)    # reassigns the value of 4 to x 


def samp4(xlist):
    #opA
    #xlist.append(5)    # creates a local variable 
    #xlist[0] = 10
    #print(xlist)

    #opB - Mutable reference binding
    #xlist = [20, 30, 40]        # this rebinds the reference and creates a local variable which has nothing to do with list4
    #xlist.append(60)

    #opC - Slight difference making huge impacts
    #xlist += [20, 30, 40]       # appends to the list4
    xlist = xlist + [20, 30, 40]    # doesn't affect the global list as it creates a new local list 

list4 = [1, 2, 3]
print('actual list:', list4)
samp4(list4)
print('after fxn:', list4)    # list4 has been updated. |   In opB, list4 remains the same because of 


