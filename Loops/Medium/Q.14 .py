# Write a program to print a diamond pattern using loops.

n = 5

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print()

for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print()



