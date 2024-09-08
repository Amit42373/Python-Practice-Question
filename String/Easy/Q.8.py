# Write a program to replace all occurrences of a character in a string with another character.


def replace_str(string, old_char, new_char):
    return string.replace(old_char, new_char)

s = input("enter a string: ")
o = input("enter a old_char: ")
n = input("enter a new_char: ")

print(replace_str(s, o, n))
