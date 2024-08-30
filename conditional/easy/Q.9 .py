# Q. Write a program to check if a number is divisible by both 5 and 11.

num = int(input("enter the number: "))

if (num % 5 == 0) and (num % 11 == 0):
    print(f"number {num} is divisible by both 5 and 11.")
else:
    print(f"number {num} is not divisible by both 5 and 11.")

