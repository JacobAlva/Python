# lambda arguments: expression
''' Small, single-line anonymous function defined without a name.
    It starts with the 'lambda', takes in arguments then the expression. '''
"""
add10 = lambda x: x + 10
print(add10(5))

# this is similar to a function to add 10, but shorter
def func_add10(x):
    return x + 10
print(func_add10(5))

# multiple arguments lambda function
mult = lambda x,y: x*y
print(mult(2,7))

# lambda usecases
# list sorting
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)      # returns a new sorted list without modifying the original
print(points2D)
print(points2D_sorted)      # by default, the list is sorted by the first index

# to sort by a different index would normally take a whole function
def sort_by_y(x):
    return x[1]
points2D_sorted_dfwf = sorted(points2D, key = sort_by_y)
print(points2D_sorted_dfwf)

# same result with a single line of lambda
points2D_sorted_df = sorted(points2D, key = lambda x:x[1])
print(points2D_sorted_df)


# to sort by sum of each tuple
p2D_sorted_sum = sorted(points2D, key = lambda x: x[0] + x[1], reverse=True)    # returns the sort in reverse order
print(p2D_sorted_sum)


# MAP
# map (func, seq)
list1 = [1, 2, 3, 4, 5]
map1 = map(lambda x: x*2, list1)
print(list(map1))

# this can also be achieved with list comprehension
list3 = [i*2 for i in list1]
print(list3)
"""


#FILTER
# filter(func, seq)
'''The function returns True/False and the filter returns all True elements'''
list4 = [1, 2, 3, 4, 5]
fila = filter(lambda x: x % 2 == 0, list4)
print(list(fila))       # cool way to get all the even numbers in a list
