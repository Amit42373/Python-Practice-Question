# Write a program to find both the minimum and maximum elements in an array using a loop.

def max_min(a):
    max = a[0]
    min = a[0]

    for i in a[1:]:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min

a = [2,5,-2,45,87,6,44]
print(max_min(a))

