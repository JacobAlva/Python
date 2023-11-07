# Errors and Exceptions
# Syntax errors, diff between syntax errors and exceptions, raising and handling exceptions, # defining your own exceptions, common types of errors, ...

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


