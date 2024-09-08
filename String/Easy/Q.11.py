# Write a program to find the frequency of a specific character in a string.

# def find_char(str):
#     a = str.count("e")
#     return a

# s = input("enter a string: ")

# print(find_char(s))

#                                       QR

def COUNT_Char(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count

s = input("enter a string: ")
c = input("enter a character you want count of: ")

print(COUNT_Char(s, c))