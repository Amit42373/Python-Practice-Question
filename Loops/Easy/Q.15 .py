# Write a program to print a right-angled triangle pattern using loops.

def pattern(n):
    for i in range(1,n+1):
        print("*" * i)

n = int(input("enter the value for n: "))
pattern(n)
