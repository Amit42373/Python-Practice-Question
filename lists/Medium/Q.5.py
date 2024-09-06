# Write a program to split a list into two lists: one containing even numbers and the other containing odd numbers.

def even_odd(list):
    even = []
    odd = []

    for el in list:
        if el % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
    return even, odd

list = [1,2,3,4,5,6,7,8,9]
e, o = even_odd(list)
print("even numbers", e)
print("odd numbers", o)