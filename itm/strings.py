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

# string slicing - to access a substring
string4 = "Welcome"
print(string4[1:6:2])     # e-m with step NOTE: index 6 "e" is excluded
print(string4[::-1 ])     # reverses the string

# string concat
string5 = "Home"
print(string4 + " " + string5)

# iterate over string with for loop
for i in string5:
    #print(i)
    pass

# check for character
if "Hom" in string5:
    print("Yes")
else:
    print("No")
"""
# strip white spaces
string6 = "   Hello World   "
print(string6)
string6.strip()     # this doesn't change the string in-place 
# i.e. update the original string, because a string is immutable
print(string6)
# to update the string, it has to be assigned
string6 = string6.strip()
print(string6)

# coverting cases
print(string6.upper())
print(string6.lower())
print(string6.lower())
print(string6.startswith("H"))
print(string6.endswith("Hel"))

# to find a character/world
# returns the index of a word/character. 
# returns -1 if not found
# this method is case sensitive
print(string6.find("W"))    

print(string6.count("o"))   # count of word/xter

# replace word/character in a string 
# this doesn't modify the string as it is immutable
# it creates a new string instead
print(string6.replace("Hel", "You"))    



