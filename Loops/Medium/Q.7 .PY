# Write a program to find all divisors of a given number using a loop.

def divisors(num):
    for i in range(1, num):
        if num % i == 0:
            print(i)
n = int(input("enter the number: "))
divisors(n)
