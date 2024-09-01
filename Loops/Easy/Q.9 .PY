# Write a program to print the Fibonacci sequence up to a given number.

def fibonacci(num):
    a = 0
    b = 1 
    c = a+b
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(num-2):
        print(c)
        a = b
        b = c
        c = a+b
n = int(input("enter the number: "))
fibonacci(n)