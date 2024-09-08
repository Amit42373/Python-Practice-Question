# Write a program to access the first, middle, and last characters of a string.

def first_middle_last(str):
    length_of_string = len(str)

    first_char = str[0]
    last_char = str[-1]
    
    if length_of_string % 2 == 0:
        middle_str = str[length_of_string // 2 -1 : length_of_string // 2 +1]
    else:
        middle_str = str[length_of_string // 2]
    
    return first_char, middle_str, last_char

s = input("enter a string: ")

F, M, L = first_middle_last(s)
print(f"first character :{F}")
print(f"middle character :{M}")
print(f"last character :{L}")