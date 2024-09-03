# Write a program to calculate the power of a number using a loop (without using built-in functions).

def power_of_num(base, expo):
    result = 1
    for _ in range(expo):
        result *= base
    return result

b =  int(input("enter the base: "))
e =  int(input("enter the exponent: "))
print(power_of_num(b, e))