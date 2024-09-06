# Write a program to rotate a list by n positions to the left.

def left_rotate(lst, n):
    n = n % len(lst)  # Ensure n is within the bounds of the list length
    return lst[n:] + lst[0:n]

# Example usage:
lst = [1, 2, 3, 4, 5]
rotated_list = left_rotate(lst, 3)
print(rotated_list)  # Output: [3, 4, 5, 1, 2]
