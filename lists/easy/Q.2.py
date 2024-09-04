# Write a program to access the first, middle, and last elements of a list.

n = int(input("enter the value of n: "))
list = []

for i in range(1, n+1):
    list.append(i)
print(list)

first_el = list[0]
last_el = list[-1]

if len(list) % 2 == 0:
    middle_el = list[len(list) // 2 -1 : len(list) // 2 + 1 ]
else:
    middle_el = list[len(list) // 2]

print(first_el)
print(last_el)
print(middle_el)