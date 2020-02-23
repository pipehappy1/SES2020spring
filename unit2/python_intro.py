help(help)
help(dir)

print('Introduction to Python')

a = "abc"
b = 'abc'
c = """abc"""

a = 1
b = 1.0

# This is a comment

alist = [1, 3, 5]
alist[0]
alist[1:]
alist.append(7)
b = alist.pop(0)

for i in alist:
    print(i + 1)

for i in range(10):
    print(i)

atuple = (1, 2, 4)

if len(atuple) > 2:
    print(len(atuple))
elif atuple[0] == 0:
    print(atuple[0])
else:
    print(atuple)

adict = {}
adist[1] = 3
adist[2] = 9

def f(x):
    return x + 1

import numpy as np


