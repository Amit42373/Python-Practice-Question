# Q.Write a program to check if a given number is an Armstrong number using if-else conditions

def is_armstrong(number):
    str_number = str(number)
    n = len(str_number)
    sum = 0 
    
    for i in str_number:
        sum = sum + int(i)**n
    if sum == number:
        print("It is an armstrong number")
    else:
        print("not an armstrong number")

number = int(input("enter the number: "))
is_armstrong(number)
