# Q. Write a program to convert a single-digit number into words (e.g., 1 -> "One").

def num_to_word():
    key = {   0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"     }
    if 0 <= num <= 9:
        return key[num]
    else:
        return "enter valid number"
    
num = int(input("enter the number: "))
print(num_to_word())
    
