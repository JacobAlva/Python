# lambda arguments: expression
''' Small, single-line anonymous function defined without a name.
    It starts with the 'lambda', takes in arguments then the expression. '''

add10 = lambda x: x + 10
print(add10(5))

# this is similar to a function to add 10, but shorter
def func_add10(x):
    return x + 10
print(func_add10(5))

# multiple arguments lambda function
mult = lambda x,y: x*y
print(mult(2,7))

