# Write a program to pair each element from two lists into a tuple.

def pair_el(list1, list2):
    return zip(list1,list2)

list1 =[1,2,3]
list2 =["amit","dee"]

print(pair_el(list1, list2))