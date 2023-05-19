# This file contains practice sessions, random codes
# Tests, ideas, etc.


# Hello world
"""
print("hello world")
"""

# Variable declaration
"""
int_var = 7 * 2
flo_var = 5.6
bol_var = False
int_var = 15 / 3 * 2 * 2 - (3 + 4)

print(int_var, flo_var, bol_var)
"""

# Round
"""
print((123 + 280)/100)
ter = (2.1/4.1)
print(round(ter, 5))
#print(round(4, ter)) #this is a wrong attempt.

# I will never let you go
"""

# String slicing
"""
mod3 = "mangowater"
ind = mod3 [3]
print(ind)
print(mod3[:3])
print(mod3[3:7])
print(mod3[5:])

nike = "Just do it!"
print(nike[10])
print(nike[5:8])
print(nike[8:])
print(nike[:4])
print("Don't " + nike[5:])
"""

# Get Type
"""
g = "4.5"
print(type(nike))
print(type(g))
print('"Hello, I am Jacob, it\'s nice to meet you"')
print("******* \n ***** \n  ***\n   *")

#name = input("Ogbeni, enter your name:")
#print("Your name is "+name+".")
#print(type(name))

sum = int(input("Enter a number:"))
print(sum+10)
print(type(sum))
"""

# String operations with functions
"""
first_str = "The number "

def fxn_name(p1, p2, p3):
    print(p1 + str(p2) + p3)


fxn_name(first_str, 5, " is an int")


def hello_world_printer():
    print("Hello world")


hello_world_printer()


def name_printer(yname):
    print("Your name is " + yname)


name = input("Enter your name:")
name_printer(name)
"""


# Calculate volume
"""
def rec_vol(length, width, height):
    return length * width * height


l = int(input("Length:"))
w = int(input("Width:"))
h = int(input("Height:"))
print("The volume of the rectangular prism is " + str(rec_vol(l,w,h)))
"""


# String comparison
"""
age = 1344
print(f'Your age is {age:10}')

x = 'got'
y = 'ys'
if x > y:
    print(y)
    print(x)
else:
    print(x)
    print(y)

print('Pizza' == 'pizza' or 100 == 1010.00)
"""


# While Loop
"""
product = 0
while product < 100:
    num = int(input("Please enter a number: "))
    product = num * 10
    print(product)
"""

# for loop
"""
#for num in [1, 2, 3, 4]:
#    print(num * 5)
x=3
for num in range(1,10,7):
    print(x)
"""

