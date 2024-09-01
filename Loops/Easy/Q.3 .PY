# Write a program to calculate the factorial of a given number using a loop.

def factorial(number):
    fact = 1
    for num in range(1, number+1):
        fact *= num
    return fact

n = int(input("enter the number: "))
print(factorial(n))