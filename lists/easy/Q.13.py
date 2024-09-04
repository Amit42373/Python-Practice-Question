# Write a program to find the index of a specific element in a list.

list = [1, 2, 'dee', "amit", 2, 5, 2, 'amit',"amit", 2, 5, 2, 'amit']

el_to_find = "amit"

if el_to_find in list:
    index = list.index(el_to_find)

print(index)