#-------------------------------------------------------
#  Square the elements of a list using map().
#-------------------------------------------------------

numbers = [1, 2, 3, 4, 5]
result = []

# 1st Method:
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
#-------------------------------------------------------

#2nd Method:

for x in numbers:
    z = x ** 2
    result.append(z)

print(result)

#-------------------------------------------------------