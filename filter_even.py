# Python function to filter even numbers:

def f_even_nums(a):
    def odd_nums(b):
        return b % 2 != 0
    
    odd_numbers = list(filter(odd_nums, a))
    return odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = f_even_nums(numbers)
print(result)