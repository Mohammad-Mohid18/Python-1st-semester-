#-------------------------------------------------------
# Transpose of a matrix.
#-------------------------------------------------------


#-------------------------------------------------------
#Function:

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed
#-------------------------------------------------------
#Main program:

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = transpose(matrix)
for x in result:
    print (x)

#-------------------------------------------------------