# Write a program to check if a given number is prime using a loop.

def prime(num):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

n = int(input("enter the number: "))
print(prime(n))
    