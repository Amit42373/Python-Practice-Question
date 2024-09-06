# Write a program to check if a list is a palindrome (reads the same forwards and backwards).

def is_palindrom(list):
    reverse_list =[]

    for el in list[-1::-1]:
        reverse_list.append(el)
    print(reverse_list)
    if list == reverse_list:
        return "palindrom"
    else:
        return "not palindrom"

list = [1,2,3,2]
rl = is_palindrom(list)
print(rl)

