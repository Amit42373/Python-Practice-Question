# Write a program to print an inverted triangle pattern using loops.

def pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n-i), end="")
        print("*" * (2 * i -1), end="")
        print("")

n = int(input("enter the value of n: "))
pattern(n)