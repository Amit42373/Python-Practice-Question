# Write a program to calculate the sum of all elements in a list.

l = [1, 2, 3, 4, 5, 7, 8, 9, 5]

s = sum(l)
print(s)

#                                 or

l = [1, 2, 3, 4, 5, 7, 8, 9]
sum = 0
for el in l:
    sum += el 
print(sum)