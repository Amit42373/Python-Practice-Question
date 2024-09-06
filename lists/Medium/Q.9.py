# Write a program to find the common elements in three different lists.

def common_el(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    common_element = set1.intersection(set2).intersection(set3)

    return list(common_element)

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
l3 = [5, 6, 7, 8, 9]

print(common_el(l1, l2, l3))

