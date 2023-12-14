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
clips(1, b=2, a=3)       # TypeError - multiple values for argument 'a' as it has been used as a positional argument 

