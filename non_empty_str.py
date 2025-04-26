# Python function to filter out empty strings from a list

def filter_empty_strings(strings):
    def non_empty(s):
        return s != ''
    
    filtered = list(filter(non_empty, strings))
    return filtered

list_of_strings = ['', 'hello', '', 'world', '']
result = filter_empty_strings(list_of_strings)
print(result)
