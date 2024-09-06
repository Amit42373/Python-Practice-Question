# Write a program to find the intersection (common elements) of two lists.

# This answer includes the set() method.

def intersection(list1, list2):
    return list(set(list1) & set(list2))

l1 = [1,2,5,7,2,"dee",45,"dee",1]
l2 = ["amit",2,7,"dee",1]
list3 = intersection(l1,l2)
print(list3)


# This is the simple method without using any built in function.

l1 = [1,2,5,7,2,"dee",45,"dee",1]
l2 = ["amit",2,7,"dee",1]

l3 = [value for value in l2 if value in l1]
print(l3)

# in this we set() the larger list and then use built in function intersection()

def intersection2(list1, list2):
    return set(list1).intersection(list2)

l1 = [1,2,5,7,2,"dee",45,"dee",1]
l2 = ["amit",2,7,"dee",1]

print(intersection2(l1, l2))