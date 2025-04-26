#-------------------------------------------------------
# Write a Python program to add two given lists and find
# the difference between them. Use the map() function.
#-------------------------------------------------------

def add_sub(x,y):
    return x + y,x - y

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = map(add_sub, list1, list2)
print(list(result))