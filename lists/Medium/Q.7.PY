# Write a program to find the second largest element in a list.

def SEC_large(l):
    L1 = max(l[0],l[1])
    L2 = min(l[0],l[1])

    for el in l[2:]:
        if el > L1:
            L2 = L1
            L1= el
        elif el > L2 and el != L1:
            L2 = el
    return L2

l = [2,54,79,3,4,59,-4,5,7,54,79]
print(SEC_large(l))
         


