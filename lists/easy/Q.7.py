# Write a program to find the length of a list without using the len() function.

list = [1, 2, 'dee', 3, 4, 5, 6, 'amit']

len_of_list = 0

for el in list:
    len_of_list += 1

print(len_of_list)