# Q. Write a program to perform basic arithmetic operations (addition, subtraction, multiplication,
#    division) based on user input using if-else conditions.

number1 = float(input("enter the number: "))
operator = input("enter operator (+,-,*,/): ")
number2 = float(input("enter the number: "))

def calculator(number1 , operator, number2):
    if operator == "+":
        print(f"{number1} + {number2} = {number1 + number2}")
    elif operator == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
    elif operator == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
    else:
        print(f"{number1} / {number2} = {number1 / number2}")

calculator(number1 , operator, number2)
    