#Write a program to slice a string to get a substring from index 2 to 5.

str = input("enter a string: ")

substring = str[2:5]
word = ''
for char in substring:
    word = word + char

print(word)