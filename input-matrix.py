#-------------------------------------------------------
# User Input Matrix.
#-------------------------------------------------------
# Function:
def input_matrix():

    length_row = int(input('enter length of the row:'))
    length_col = int(input('enter length of the column:'))

    matrix = [[0 for i in range(length_col)] for j in range(length_row)]

    for x in range(length_row):
        for y in range(length_col):
            matrix[x][y] = int(input('enter elements: '))

    return matrix

#-------------------------------------------------------
# Main Program:

matrix1 = input_matrix()
for i in matrix1:
    print (i)