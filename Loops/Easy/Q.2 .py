# Write a program to find the sum of the first N natural numbers.

def first_n(number):
    sum = 0
    for num in range(number+1):
        sum += num
    return sum

n = int(input("enter the number: "))
print(first_n(n))