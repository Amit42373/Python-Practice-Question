# Write a program to count how many times a specific element appears in a list.

list = [1, 2, 'dee', "amit", 2, 5, 2, 'amit',"amit", 2, 5, 2, 'amit']

print(list.count(2))  # by list method

#                               OR 

spec_el = "amit"
count = 0 
for el in list:
    if el == spec_el:
        count += 1 
print(count)




