# Write a program to remove all duplicate elements from a list.

l = [1,2,5,7,2,"dee",45,"dee",1]

unique_l = []

for i in l:
    if i not in unique_l:
        unique_l.append(i)
print(unique_l)

