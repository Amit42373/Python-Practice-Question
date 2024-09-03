# Write a program to check if a given number is an Armstrong number using a loop.

def is_armstrong(number):
    str_number = str(number)
    n = len(str_number)
    is_strong = 0

    for num in str_number:
        is_strong += int(num)**n
    if is_strong == number:
        print("armstrong")
    else:
        print("not armstrong")

n = int(input("enter the number: "))
is_armstrong(n)


