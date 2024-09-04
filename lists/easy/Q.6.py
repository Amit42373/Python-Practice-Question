# Write a program to reverse a given list using slicing and a loop.

list = [1, 2, 3, 4, 5, 6]
rev_list = []

for el in list[5::-1]:
    rev_list.append(el)

print(rev_list)


