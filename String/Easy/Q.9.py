# Write a program to reverse a given string.

def reverse(str):
    reverse_str = ""
    for char in str:
        reverse_str = char + reverse_str
    return reverse_str


str = "amit"
print(reverse(str))