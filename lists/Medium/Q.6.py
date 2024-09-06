# Write a program to flatten a nested list (a list within a list) into a single list.

l = [1, [2, [3, 4]], 5]

def flatten(l):
    flatlist = []
    for el in l:
        if type(el) is list:
            flatlist.extend(flatten(el))

        else:
            flatlist.append(el)
    return flatlist

print(flatten(l))