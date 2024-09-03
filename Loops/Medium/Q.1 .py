# Write a program to find the second largest element in an array using a loop.

def sec_largest(l):
    lar = max(l[0], l[1])
    sec_lar = min(l[0], l[1])
    for i in l[2:]:
        if i > lar:
            sec_lar = lar
            lar = i 
        elif (i > sec_lar) and (i != lar) :
            sec_lar = i
    return sec_lar
            
a = int(input("enter the number of element you want in your list: "))
l = []
for i in range(a):
    el = int(input("enter the element: "))
    l.append(el)
print(sec_largest(l))
