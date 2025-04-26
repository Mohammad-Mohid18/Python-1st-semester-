# Read a file line by line store it into an array.

def read(file_name):
    list = []
    f = open(file_name, 'r')
    r = f.read()
    list.append(r)
    # for line in f:
    #     list.append(line.strip())
    print(list)


read('file handling/practice.txt')