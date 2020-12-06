import os

upath = input('give a path : ')
print(os.walk(upath))
for r,d,f in os.walk(upath):
    for x in f:
        print(x)