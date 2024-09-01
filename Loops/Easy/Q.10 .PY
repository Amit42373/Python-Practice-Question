# Write a program to find the largest element in an array using a loop.

def is_largest():
    array = [1,2,3,-1,55,5,4,8,7]
    largest = 0 
    for i in array:
        if i > largest:
            largest = i
    print(f" The largest element in array is: {largest}.")

is_largest()    




