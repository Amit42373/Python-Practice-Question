# Write a program to find the elements that are in one list but not in another.

l1 = [1,2,5,7,2,"dee",45,"dee",1]
l2 = ["amit",2,7,"dee",1,"potter"]

unique_in_list1 = list(set(l1) - set(l2))
print(f"The element that are in list 1 but not in list 2:\n{unique_in_list1}")

unique_in_list2 = list(set(l2) - set(l1))
print(f"The element that are in list 2 but not in list 1:\n{unique_in_list2}")