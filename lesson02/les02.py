# coding: utf-8

print("Добро пожаловать на курс Python Quick Start!")

name = input("Your name: ")

print(name, ", wellcome in the world of Python")

answer = input("Let's get to work? (Y/N) ")

# PEP-8
if answer == 'y':
    print("Hooray!")
elif answer == "n":
    print("Buy!")
else:
    print("Unknown answer")
