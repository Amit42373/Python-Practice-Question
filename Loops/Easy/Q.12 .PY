# Write a program to print all even numbers between 1 and 100.

def even_num(num):
    for i in range(1,num+1):
        if i % 2 == 0:
            print(i)

num = int(input("enter the number: "))
even_num(num)