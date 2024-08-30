# Q. Write a program to determine if a triangle is equilateral, isosceles,
#     or scalene based on the lengths of its sides.

x = int(input("enter the side x: "))
y = int(input("enter the side y: "))
z = int(input("enter the side z: "))

# Valid Triangle Check: A triangle is valid if the sum of any two sides is greater than the third side. 
def triangle():
    if (x+y > z) and (y+z > x) and (z+x > y):      
        if (x != y) and (x != z):
            print("scalene triangle")
        elif (x == y) and (x == z):
            print("equilateral triangle")
        else:
            print("isosceles triangle")
    else:
        print("the sides do not form a valid triangle.")

triangle()
