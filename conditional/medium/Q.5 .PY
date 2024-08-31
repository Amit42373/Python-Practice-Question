# Q. Write a program to solve a quadratic equation and determine the nature of its roots 
#    (real and equal, real and distinct, or imaginary).

#  general form of a quadratic equation: (ax**2 + bx + c = 0)
 
import math

a = float(input("enter the coefficiant a: "))
b = float(input("enter the coefficiant b: "))
c = float(input("enter the coefficiant c: "))

# Calculate the discriminant
D = (b**2) - (4*a*c)

#  Determine the nature of the roots and compute the roots

if D > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(D)) / 2*a
    root2 = (-b - math.sqrt(D)) / 2*a
    print("the roots are real and distinct")
    print("root 1 :", root1)
    print("root 2 :", root2)
elif D == 0:
    # one real root
    root = -b / 2*a
    print("the root are real and equal")
    print("root:", root)
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-D) / (2 * a)
    print("The roots are imaginary (complex).")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")




