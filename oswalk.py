import os

upath = input('give a path : ')
for r,d,f in os.walk(upath):
    print(f)