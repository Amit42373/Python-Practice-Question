# Write a program to check whether a number is positive, negative, or zero using if-else conditions.

def prog():
    num = int(input("enter the number: "))
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    if num == 0:
        return "zero"

print(prog())