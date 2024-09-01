# Write a program to count the number of digits in a given number.

def count_digit(number):
    count = 0
    for i in number:
        count += 1 
    return count
n = input("enter the number: ")
print(count_digit(n))

#                                  OR

def count_digit(number):
    return len(number)
n = input("enter the number: ")
print(count_digit(n))