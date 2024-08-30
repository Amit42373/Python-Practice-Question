# Write a program to determine if a given year is a leap year.

year = 2023

def leap():
    if (year % 4 ==0) and (year % 100 != 0):
        print("yes, it is a leap year")
    else:
        print("not a leap year")

leap()