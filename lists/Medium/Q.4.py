# Write a program to sort a list in ascending and descending order without using the sort() function.

# ascending order

list1 = [9,2,345,-5,7,78,3]

print("orignal_list: ", list1)

for i in range(0, len(list1)):
    for j in range(i+1,len(list1)):
       if list1[i] > list1[j]:
           list1[i], list1[j] = list1[j],list1[i]
           print(list1)

print("sorted list: ", list1)



# Descending order

list1 = [1,2,345,-5,7,78,3]

print("orignal_list: ", list1)

for i in range(0, len(list1)):
    for j in range(i+1,len(list1)):
       if list1[i] < list1[j]:
           list1[i], list1[j] = list1[j],list1[i]

print("sorted list (desc): ", list1)