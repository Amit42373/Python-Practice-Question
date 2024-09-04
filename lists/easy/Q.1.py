# Write a program to create a list of the first 10 natural numbers.

n = int(input("enter the value of n: "))
list = []

for i in range(1, n+1):
    list.append(i)
print(list)

