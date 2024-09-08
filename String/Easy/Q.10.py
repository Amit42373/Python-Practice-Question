# Write a program to check if a string contains only numeric characters.

s = input("enter a string: ")

def is_numeric(str):
    return str.isdigit()

print(is_numeric(s))