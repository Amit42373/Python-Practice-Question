# Write a program to check if a given number is a perfect number (sum of divisors equals the number).

def is_perfect(num):
    sum = 0
    for i in range(1, num-1):
        if num % i == 0:
            sum += i
    if sum == num:
        print(f"{num} is the perfect number.")
    else:
        print(f"not a perfect number.")

num = int(input("enter the number: "))
is_perfect(num)
