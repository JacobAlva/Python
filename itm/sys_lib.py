# this file contains several examples of uses of the sys library.


import sys

# compare the size of tuple and list in "bytes"
tuple8 = ("what", "is", "your", "name?", 373, "watermelon")
list3 = ["what", "is", "your", "name?", 373, "watermelon"]
print(sys.getsizeof(tuple8), "bytes")
print(sys.getsizeof(list3), "bytes")
# the results show that a tuple is more memory efficient




# compare the size of two functions using the 'getsizeof' method
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):    # more memory efficient as it doesn't require the list
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))