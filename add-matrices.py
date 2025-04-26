#-------------------------------------------------------
# Adding two matrices.
#-------------------------------------------------------


#-------------------------------------------------------
# Function:
def add(a,b):
    row_a = len(a)
    col_a = len(a[0])
    row_b = len(b)
    col_b = len(b[0])

    if row_a != row_b or col_a != col_b:
        return "Matrices can't be added"
    
    result = [[0 for _ in range(col_a)] for _ in range(row_a)]

    for i in range(row_a):
        for j in range(col_a):
            result[i][j] = a[i][j] + b[i][j]

    return result

#-------------------------------------------------------
# Main Program:
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2 = [
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

result = add(mat1, mat2)

for row in result:
    print(row)
    
#-------------------------------------------------------