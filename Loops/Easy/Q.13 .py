# Write a program to find the greatest common divisor (GCD) of two numbers using loops.

def GDC(a, b):
    hcf = 0
    if a > b :
        smallest = b
    else:
        smallest = a

    for i in range(1, smallest+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf

a = int(input("enter the number: "))
b = int(input("enter the number: "))
print(GDC(a, b))