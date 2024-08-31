# Q. Write a program to compare two strings lexicographically using if-else conditions.

def is_lexicographically():
    if string1 < string2:
        print(f"{string1} comes before {string2} lexicographically.")
    elif string1 > string2:
        print(f"{string1} comes after {string2} lexicographically.")
    else:
        print(f"{string1} is equals to {string2} lexicographically.")

string1 = input("enter the string: ")
string2 = input("enter the string: ")

is_lexicographically()