# Write a program to remove duplicates from an array using loops.

def remove_dup(array):
    unique_array = []

    for el in array:
        if el not in unique_array:
            unique_array.append(el)
    return unique_array

a = [1, 2, 3, 2, 4, 5, 3, 6, 1]

print(remove_dup(a))

