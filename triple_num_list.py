#-------------------------------------------------------
# Triple the nums of the lists.
#-------------------------------------------------------

nums = []

len_list = int(input('enter the length of the list:'))

for i in range(len_list):
    elements = int(input('enter the nums of the list:'))
    nums.append(elements)

print('original numbers',nums)

result = map(lambda x: x*3 , nums)     # Accessing each elementof the list and multiplyingit with 3.

print('tripled the numbers of the list=',list(result))

#-------------------------------------------------------