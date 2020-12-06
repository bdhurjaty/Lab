import os

userpath = input("enter ur path: ")

if os.path.isfile(userpath):
    print("given is a file")
elif:
    os.path.isdir(userpath):
    print("given is a dir")