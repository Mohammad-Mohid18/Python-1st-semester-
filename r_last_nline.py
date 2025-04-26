# Write a Python program to read last n lines of a file.

def read_nlines(file,lines):
    strt = open(file, 'r')
    content = strt.readlines()[-lines:]
    print(content)
    strt.close()

path = 'file handling/practice.txt'
lines = int(input('enter the number of lines to read:'))
read_nlines(path, lines)