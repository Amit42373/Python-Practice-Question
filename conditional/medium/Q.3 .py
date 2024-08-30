# Q. Write a program to check if a given number is prime using if-else conditions.

number = int(input("enter the number: "))

is_prime = True

if number <=  1:
    is_prime = False
else:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            
print(number, "is a prime number:", is_prime)
