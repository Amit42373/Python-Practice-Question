# Write a program to find the highest common factor (HCF) of two numbers using loops

def hcf(n1, n2):
    result = 0
    if n1 > n2:
        smallest = n2
    else:
        smallest = n1
    
    for i in range(1, smallest+1):
        if (n1 % i == 0) and (n2 % i == 0):
            result = i
    return result
        
a = int(input("enter the number: "))
b = int(input("enter the number: "))
print(hcf(a, b))