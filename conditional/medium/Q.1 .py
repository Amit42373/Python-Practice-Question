# Q. Write a program to check if a given character is uppercase or lowercase using if-else conditions.


char = input("enter a character: ")

if len(char) == 1 and char.isalnum():
    if char == char.lower():
        print("lower case")
    else:
        print("UPPER CASE")
else:
    print("please enter a single character.")