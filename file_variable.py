# Read a file line by line store it into a variable

def fil(name):
    with open(name, 'r') as fill:
        data = fill.read()
        print(data)

fil('file handling/practice.txt')

# Read a file line by line and store it into a list

# myfile = open('file handling/practice.txt', 'r')
# lines = myfile.read()
# print(lines)