# long words:

def long_words(a):
    return len(a) > 5

words = ['hello', 'world', 'python', 'programming', 'is', 'awesome']

long_words_list = list(filter(long_words, words))
print(long_words_list)