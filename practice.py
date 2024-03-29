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

# While Loop (Condition-controlled pretest Loop)
"""
counter = int(input('Enter number:'))
a = counter
summed = 0

while counter > 0:
    summed += counter
    counter-=1
print(summed)
"""

# For loop (Count-controlled pretest loop)
"""
strn = input('please enter your word:')
sum = 0
for char in strn:
    sum += 1

print(strn, "\n", "The number of characters in this string are: ", sum)

tr = range(5,10)
for a in tr:
    print(a)
"""

# float decimal format and approx
"""
num = 1234567.456
print(f'{num:,.1f}')
"""

# Get a salesperson's sales and commission rate.
"""
while True:
    try:
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate: '))
        # Calculate the commission.
        commission = sales * comm_rate
        # Display the commission.
        print('The commission is $', format(commission, ',.2f'), sep='')
        break
    except:
        print("Please enter a valid input.")
"""

# Score grader
"""
score = int(input("Please enter your score: "))

if score >= 90:
    print("Your score is ", score, "and your grade is A")
elif score >= 80:
    print("Your score is ", score, "and your grade is B")
elif score >= 70:
    print("Your score is ", score, "and your grade is C")
elif score >= 60:
    print("Your score is ", score, "and your grade is D")
else:
    print("Your score is ", score, "and your grade is F")
"""

# While loop
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

# User controlled for loop
"""
init_value = int(input("Please enter the initial value: "))
lim = int(input("Please enter the ending limit: "))
step_val = int(input("Please enter the stepping value: "))

for x in range(init_value,lim, step_val):
    print(x)
"""

# Table using "For"
"""
cost = 1
print("PID \t Cost")
for i in range (1, 6):
    print(i, " \t \t $", i * 5)
"""


# Class average - for Loop
"""
total = 0
number_of_students = int(input("Please enter the number of students in your class: "))

for x in range(number_of_students):
    student_score = float(input("Please enter the student score: "))
    total = total + student_score

average_score = total / number_of_students

print(f'You have a total of {number_of_students} students in your class')
print(f'The total score of the {number_of_students} students is {total:.2f}')
print(f"The average score for the {number_of_students} students is {average_score:.2f}")
"""

# Input validation - While loop (condition based)
"""
age = float(input("Please enter your age: "))

while 0 < age > 125:
    print("Please enter a valid age: ")
    age = float(input("Please enter your age: "))

print("Your age is: ", age)
"""

# Iterating loop (for)
"""
for i in range(5):
    print(i)
    for j in range(5):
        print(i, "x", j, "=", i*j)
"""

# ***************************
### CHAPTER 5 - FUNCTIONS ###

# Function declaration and call
"""
def myPrint():
    print("Hello World")

def yourPrint():
    print("Hello Charlotte my love ^:)^")

def main():
    myPrint()
    yourPrint()
"""


# String compare operations
"""
s = "New York"
y = "Boston"
if s>y:
    print(s)
else:
    print(y)
"""


# Class Example - for loop
"""
def foo():
    a = 10
    b = 20
    c = 0
    for i in range (3):
        c += (a+b)
        print(c)
foo()
"""

# Passing Arguments to Functions
"""
def main():
    a = 5
    b = 6
    #show_double(a)
    my_add(a, b)
    #my_sub(a, b)
    #my_mul(a, b)
    #my_div(a, b)
    #print("r=", a, "b= ", b)
    total = my_add(a, b)
    print("Total = ", total)

# def show_double(number):
#     result = number * 2
#     print(result)
#     return result

def my_add(x, y):
    print(x + y)
    return (x + y)

def my_sub(x, y):
    if x > y:
        print(x - y)
    else:
        print(y - x)

def my_mul (x, y):
    print(x * y)

def my_div(x, y):
    """"""
    if y != 0:
        print(x/y)
    else:
        print("You cannot divide by zero")
    """"""
    while y == 0:
        print("You cannot divide by zero")
        y = int(input("Enter a value for b: "))
    print(format(x/y,'.2f'))

main()

"""


# ***************************
### CHAPTER 6 - FILES AND EXCEPTIONS ###

# File operations - write, read, append
"""
def main():
    # open file for writing
    infile = open('philosopher.txt', 'w')

    # write three lines
    infile.write('John Doe\n')
    infile.write('Jane Doe\n')
    infile.write('Junior Doe\n')

    # close file after you are done writing
    infile.close()

    # open file for reading
    infile = open('philosopher.txt', 'r')

    # read three lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # close file after you are done reading
    infile.close()

    # append to philosopher
    note = open('philosopher.txt', 'a')
    note.write('It worked \n')
    note.close()


    # print
    print(line1)
    print(line2)
    print(line3)

if __name__ == '__main__':
    main()
"""

# Loops to process files
"""
# Program 6-8 and 6-9, page 321-324

# Step 1, enter data by asking user how many data entries to process
# Step 2, read the data

def main():
    num_days = int(input("How many records do you want to process: "))

    #### Writing to file ####
    sales_file = open('sales.txt', 'w')

    for count in range(1, num_days + 1):
        sales = float(input(f'Enter the sales for day # {count}: '))
        sales_file.write(f'{sales}\n')

    sales_file.close()

    #### Reading & Printing from the file ####
    sales_file = open('sales.txt', 'r')

    count = 0
    line = sales_file.readline()

    while line != '':
        count += 1
        amount = float(line)
        print(f'The sales amount for day # {count} is ${amount:.2f} \n')
        line = sales_file.readline()

    sales_file.close()

if __name__ == '__main__':
    main()
"""


# Try/Except with for loop
"""
def main():
    for x in range (3):
        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))

        try:
            result = num1 / num2
            print(f'{num1} / {num2} = {result:.2f}')
        except:
            print('You cannot divide by 0')

if __name__ == '__main__':
    main()
"""


# ***************************
### CHAPTER 7 - LIST AND TUPLES ###


# Graph with matplotlib
"""
import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Build the graph
    plt.plot(x_coords, y_coords, marker='')

    # Add title
    plt.title('Sample Data')

    # Add labels to the axis
    plt.xlabel('Product')
    plt.ylabel('Price')

    #Set the axis limits
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    # Add grid
    plt.grid(True)

    # Display the graph
    plt.show()

# Display the graph
if __name__ == '__main__':
    main()
"""


# Table with list
"""
def main():
    list_size = 5
    a = [0] * list_size
    b = [0] * list_size
    print(f'A = {a} \nB = {b}')

    c = foo(a, b, list_size)

    print(f'A = {a} \nB = {b}')
    fool(a, b, c, list_size)
    print("\n Good bye")

def foo(arg_a, arg_b, arg_size):
    c = [0] * arg_size
    for i in range(arg_size):
        arg_a[i] = i * 3
        arg_b[i] = i * 2
        c[i] = arg_a[i] + arg_b[i]
    return c

def fool(a, b, c, arg_size):
    print("A\tB\tC")
    print("===========")
    for i in range(arg_size):
        print(f'{a[i]}\t{b[i]}\t{c[i]}')

if __name__ == '__main__':
    main()
"""

 
 # table print format
var: str = 'Python'     # type annotation | provides a hint of the variable type
print(f'{var:_<20}')
#print(type(var))