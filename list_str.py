#-------------------------------------------------------
# Convert a list of integers, tuple of integers in a 
# list of strings
#-------------------------------------------------------
nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)


result_list = list(map(str, nums_list))

result_tuple = tuple(map(str, nums_tuple))

print(result_list)

print(result_tuple)

#-------------------------------------------------------