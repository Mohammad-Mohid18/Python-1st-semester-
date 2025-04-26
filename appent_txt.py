# Append text to a file and display the text.

strt = open('file handling/practice.txt','a')
strt.write('\nnew line added')
strt.close()

content = open('file handling/practice.txt','r')
print(content.read())