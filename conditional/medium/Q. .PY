# Q. Write a program to check if a given character is a digit using if-else conditions

def is_digit():
    if "0" <= char <= "9":
        print("The given character is a digit.")
    else:
        print("The given character is not a digit.")

char = input("Enter a character: ")

if len(char) == 1:
    is_digit()
else:
    print("Invalid input. please enter a single character.")