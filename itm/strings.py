# Strings: ordered, immutable, used for text representation

# A string is enclosed in single, double or triple quotes
# regular string
string0 = "This is a string"
string0a = 'This is also a string'      # single or multi quotes

# Multi-line string
string1 = """This is a
multiline string"""
#print(string1)

# if you want them printed out on the same line, use an escape
string2 = """This is a \
multi line string on one line"""
#print (string2)

"""
# string indexing
# A string share a number of similarities with a tuple
string3 = "Hello World"
#print([i+"4" for i in string3])
print(string3[2])   # third character
print(string3[-1])  # last character

# string assignment
string3[0] = "h"    # this operation cannot work because a string is immutable
"""
# string slicing - to access a substring
string4 = "welcome"
print(string4[1:6:2])     # e-m with step NOTE: index 6 "e" is excluded
print(string4[::-1 ])     # reverses the string