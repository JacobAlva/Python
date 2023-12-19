# Copying mutable elements using the copy module
# Diff between the shallow and deep copy

# Shallow copy: one level deep, only references of nested child objects
# Deep copy: full independent copy

# shallow copy
"""
# does not affect immutable elements
a = 5
cop_a = a   # references the same memory location as a
cop_a = 6   # creates a new variable 
print(a)
print(cop_a)

# mutable element
b = [1, 2, 3]
cop_b = b
cop_b.append(4)     # both b and cop_b are affected by the change
print(b)
print(cop_b)        
"""

import copy
"""
list1 = [1, 2, 3, 4]
#cpy = copy.copy(list1)         # copy module and fxn
#cpy = list1.copy()              # copy method
#cpy = list(list1)               # list constructor
cpy = list1[:]                  # list splicing

cpy[0] = -1
print(list1)
print(cpy)
"""
''' All these shallow copy methods only work if the iterable is just one level deep'''

# Deep copy
# For example    
"""
list2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
#newlst = copy.copy(list2)
#newlst = list2.copy()
#newlst = list2[:]
''' All of these won't work '''
newlst = copy.deepcopy(list2)       # deep copy

newlst[1][1] = -1
print(list2)
print(newlst)
"""

# ex 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee



p1 = Person('Alex', 55)
p2 = Person('Joe', 27)
#p2 = p1                # simple assignment
#p2 = copy.copy(p1)      # shallow copy

#p2.age = 30
#print(p1.age)
#print(p2.age)

company = Company(p1, p2)
#company_clone = copy.copy(company)      # shallow copy. Won't work
company_clone = copy.deepcopy(company)     # works

company_clone.boss.age = 60

print(company.boss.age)
print(company_clone.boss.age)

