# Write a program to check if a given string is a palindrome.

str = input("enter a string: ")

is_palindrome = True

reverse_str = ""

for char in str:
    reverse_str = char + reverse_str
if str != reverse_str:
    is_palindrome = False

print(is_palindrome)


