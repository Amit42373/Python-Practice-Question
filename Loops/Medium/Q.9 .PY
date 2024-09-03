# Write a program to print numbers from N to 1 using a loop.
def reverse(n):
    for num in range(n, 0, -1):
        print(num)

n = int(input("enter the number: "))
reverse(n)