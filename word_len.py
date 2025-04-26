# Grouping words by there lengths:

def group_words(word_list):
    dict = {}
    for word in word_list:
        length = len(word)
        if length not in dict:
            dict[length] = [word]
        else:
            dict[length].append(word)
    
    return dict

len_dict = int(input('enter the length of the dictionary:'))

words_list = []

for x in range(len_dict):
    word = input('enter the words: ')
    words_list.append(word)
    
result = group_words(words_list)
print(result)
# for length, words in result.items():
#     print(f'{length} {words}')
