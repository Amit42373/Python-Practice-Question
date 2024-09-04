# Write a program to find the maximum and minimum elements in a list.

list = [1,2,3,48,5,8,9,7,5,4,6,-5,5]

def max_min(list):
    max = list[0]
    min = list[0]

    for el in list:
        if el > max:
            max = el
        elif el < min:
            min = el
    return max, min

max, min = max_min(list)
print(f"the maximum value is: {max}\nand minimum value is: {min}.")

#                    OR  by max and min function

list = [1,2,3,48,5,8,9,7,5,4,6,-5,5]
a = max(list)
b = min(list)

print(a)
print(b)
