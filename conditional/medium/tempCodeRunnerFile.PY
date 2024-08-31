STR = input("enter a word: ")
REV_STR = STR[::-1]

print(REV_STR)

if STR == REV_STR:
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")