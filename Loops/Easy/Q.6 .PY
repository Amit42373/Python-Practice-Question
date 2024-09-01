# Write a program to reverse the digits of a given number.

def reverse_digit(number):
    rev_num = ""
    for i in number:
        rev_num = i + rev_num
    return int(rev_num)

n = input("enter the number: ")
print(reverse_digit(n))
