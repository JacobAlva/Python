# Errors and Exceptions
# Syntax errors, diff between syntax errors and exceptions, raising and handling exceptions, # defining your own exceptions, common types of errors, ...

"""
# SYNTAX ERROR
''' Occurs when the parser detects a syntactically incorrect statement.'''
# a = 5 print(a))       # there are two syntax errors here

''' A syntactically correct statement might still raise an exception error. There are
    different types defined in this class e.g. TypeError, NameError, IndexError, IOError, etc.
'''

# a = 5 + "5"     # TypeError: unsupported operand

# import somemodule   # ModuleNotFoundError - subclass from the ImportError

# b = c       # NameError: 'c' is not defined

#d = open('somefile.txt')        # FileNotFoundError

e = [1,2,3,4]
# print(e.remove(0))      # ValueError 0 not in list
# print(e[5])     # IndexError - out of range

f = {'name': 'Jon', 'last': 'Jenas'}
# print(f['age'])     # KeyError


# RAISING AN EXCEPTION
''' Force an exception to occur when a certain conditon is met'''

# raising with if statement
# g = int(input("Enter a number: "))
# if g < 0:
#    raise Exception('Value should be positive.')

# raising with assert
h = 4
assert (h % 2 == 0), "Value is not even."     # can be used for any specified condition
"""

# HANDLING EXCEPTIONS
''' Ensures the code doesn't stop at a syntax error but continues to run the except block'''
# try - except
try:
    i = 5/0    # ZeroDivisionError
    j = 5 + "10"

# to print out a generic error message, good for security and should be same for all errors
#except:
#    print("An error has occured.")

# to catch the type of exception and print out
#except Exception as ex:
#    print(ex)

# you can specify the type of exception to catch if you know it
except ZeroDivisionError as ex:
    print(ex)

# you can specify multiple excepts for a single try
except TypeError as ex:     # this will print if the first except is not caught
    print(ex)