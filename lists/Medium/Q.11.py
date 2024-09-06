# Write a program to find the cumulative sum of the elements in a list.

list = [22,87,65,31,455,99]

def sum_list(list):
    sum_of_list = 0
    for el in list:
        sum_of_list += el
    return sum_of_list

print(sum_list(list))