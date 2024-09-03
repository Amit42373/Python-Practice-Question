# Write a program to find the least common multiple (LCM) of two numbers using loops.

def Lcm_of_num(num1, num2):
    if num1 > num2:
        greatest = num1
    else:
        greatest = num2

    for _ in range(greatest):
        if (greatest % num1 == 0) and (greatest % num2 == 0):
            break
        greatest += 1
    return greatest

a = int(input("enter the number: "))
b = int(input("enter the number: "))

print(Lcm_of_num(a, b))