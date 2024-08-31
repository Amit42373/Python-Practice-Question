# Q. Write a program to check if a given number is a perfect square using if-else conditions.

def is_perfect_square():

    sqr_root = int(num**(1/2))       # we also use "math.isqrt()" 

    if sqr_root**2 == num:
        print("perfect square.")
    else:
        print("not a perfect square.")

num = int(input("enter the number: "))
is_perfect_square()

#                              OR

import math

def is_perfect_square():

    sqr_root = math.sqrt(num)
   
    if sqr_root.is_integer():
        print("perfect square.")
    else:
        print("not a perfect square.")

num = int(input("enter the number: "))
is_perfect_square()

