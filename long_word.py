# Write a python program to find the longest words.

def find_longest(filename):
    f = open(filename, 'r')
    r = f.read().split()
    longest_word = []
    max_length = 0
    for word in r:
        word_length = len(word)
        if word_length > max_length:
            longest_word = [word]
            max_length = word_length
        elif word_length == max_length:
            longest_word.append(word)

    return longest_word

print(find_longest('file handling/practice.txt'))