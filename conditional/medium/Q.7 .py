# Q. Write a program to determine if a given year is a century year (a year that ends in 00).

def is_century():
    if year % 100 == 00:
        return "It is a century year"
    else:
        return "It is not a century year"
    
year = 2010
print(is_century())