# Write a program to check if a given number is a palindrome.

def is_pelendrome(number):
    rev_num = ""
    for i in number:
        rev_num = i + rev_num
    if number == rev_num:
        print("given number is a palindrome.")
    else:
        print("given number is not a palindrome.")
    
n = input("enter the number: ")
is_pelendrome(n)