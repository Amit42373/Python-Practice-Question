# Write a program to find the length of a string.

str = input("enter a string: ")

len_of_string = 0

for char in str:
    len_of_string += 1

print(len_of_string)


#                     OR

print(len(str))