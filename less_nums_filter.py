# Write a Python function that filters out all elements 
# less than or equal than a specified value from a list 
# of numbers using the filter function.

def filtering_nums(a,b):
    def range_filter(a):
        return a <= b
    
    filtered = list(filter(range_filter,a))
    return filtered

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
limit = 5
result = filtering_nums(numbers, limit)
print(result)