# Write a program to generate the multiplication table for a given number.

def table_of(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")

n = int(input("enter the number: "))
table_of(n)