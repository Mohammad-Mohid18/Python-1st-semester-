#-------------------------------------------------------
# Write a Python program to create a list containing the
# power of said number in bases raised to the corresponding
# number in the index using Python map.
#-------------------------------------------------------

number = [10,20,30,40]
indices = list(range(len(number)))
result = []

# 1st method:

for x in number:
    for y in indices:
        if number.index(x) == y:
            z = x ** y
            result.append(z)

print(result)
#-------------------------------------------------------

result = list(map(lambda x,y: x ** y, number ,indices))
#-------------------------------------------------------

print(result)

#-------------------------------------------------------