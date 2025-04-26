#-------------------------------------------------------
# Union of two lists.
#-------------------------------------------------------

#-------------------------------------------------------
# Function for comnbining two lists
def union(l1,l2):
    result = []
    for i in l1:
        if i not in result:
            result.append(i)

    for j in l2:
        if j not in result:
            result.append(j)

    return result

#-------------------------------------------------------
# Function for sorting the final result
def sort(result):
    for i in range(len(result)-1,0,-1):
        for j in range(i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    return result

#-------------------------------------------------------
# Main Program:

#First List;

len1 = int(input('enter the length of list 1:'))
list1 = []
for length1 in range(len1):
  inp1 = int(input('enter the numbers of the list:'))
  list1.append(inp1)
print('list1=',list1)

#Second list:

len2 = int(input('enter the length of the list2:'))
list2 = []
for length2 in range(len2):
  inp2 = int(input('enter the numbers of list:'))
  list2.append(inp2)
print('list2=',list2)

result = union(list1,list2)
sort(result)
print('union of the 2 lists=',result)