# Variable

x = 1
x
type(x)
x = 1.1
x
type(x)
1+1j
x + 1
x = 'abc'
x
x = "abc"
x = """abc"""
x = 'abc"abc"'
x
x + 'bcd'
x = "   sfdsf   "
x.strip()
x
dir(x)
help(x.strip)
help(help)
help(dir)
# this is a comment.
print("Hello class!")

# Control flow, branching
x = 1
if x == 1:
    print("x is {}".format(x))
else:
    print("No way")

if x == 1:
    print('x==1')
elif x == 0:
    print('x == 0')
else:
    print('x')

type(x==1)
x == 1 and 2 == int('2')
x == 1 or 2 == int('1')
not x == 1
a = [1, 2, 3]
1 in a
x = None
x == 1
x == 0
type(x)
x is None
x is not None

# List, tuple, and dict

x = [1, 2, 3, 4, 5]
x
type(x)
x[0]
x[0] = -1
x
x[:2]
type(x[:2])
for elem in x:
    print(str(elem + 1))

for index in range(len(x)):
    print(str(x[index]))

[print(str(x[index])) for index in range(len(x))]
x
y = tuple(x)
y
y[0]
y[0] = 1
y = list(x)
y
z = dict()
z = {}
z[0] = 1
z[1] = 2
z
z[0]
for key, value in z.items():
    print(str(key), str(value))



dir(z)
-1 in z
1 in z

# Control flow, loop

for x in [1, 2, 3, 4, 5]:
    if x == 2:
        continue
    elif x == 4:
        break
    else:
        print(x)
else:
    print('no find')

for x in [1, 2]:
    print(x)
else:
    print('no find')

i = 0
while i < 5:
    print(i)
    i += 1

# Function and module

def count_char(fn,):
    import os.path
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:
            total = 0
            for line in fh:
                total += len(line)
            return total

count_char('./unit2/readme.md')
import os.path
