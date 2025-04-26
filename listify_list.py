#-------------------------------------------------------
# Use map function to listiffy the given strings of a
# liat individually.
#-------------------------------------------------------

strings = ['apple', 'banana', 'cherry']
result1 = []
result2 = []

for x in strings:
    result1.append(list(x))
for y in result1:
    result2.append(list(y))

print(result2)
#-------------------------------------------------------