# Q. Write a program to find the largest of three numbers using if-else conditions.

num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
num3 = int(input("enter the number 3: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is a largest number")
elif (num2 > num1) and (num2 > num3):
    print(num2, "is a largest number")
else:
    print(num3, "is a largest number")