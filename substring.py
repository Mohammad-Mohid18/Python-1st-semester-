# Python function to filter strings with a specific substring.

def extract(a,b):
    def has_substring(s):
        return b in s
    
    filtered = list(filter(has_substring, a))
    return filtered

list_of_strings = ['hello', 'world', 'programming', 'is', 'awesome']
substring = 'e'
result = extract(list_of_strings, substring)
print(result)