# Python program to extract names starting with vowels

def extract(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    names = []
    for i in a[0]:
        if i[0].lower() in vowels:
            names.append(i)
    return names

students = ['john','steve','harry','alias','erie','illa']
result = filter(extract,students)
print(list(result))