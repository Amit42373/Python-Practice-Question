# Write a program to print all prime numbers between 1 and 100 using a loop.

def prime(n):
    for num in range(n+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

prime(10)
