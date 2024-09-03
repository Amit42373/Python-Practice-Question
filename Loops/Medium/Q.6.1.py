# Full Pyramid Patterns in Python using Loop

def pattern(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        print("*" * (2*i - 1), end="")
        print("")

row_no =  int(input("enter the number of rows: "))
pattern(row_no)
