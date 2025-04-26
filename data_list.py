#-------------------------------------------------------
# Create a new list taking specific elements from a 
# tuple and convert a string value to integer
#-------------------------------------------------------

# 1st Method:

student_data  = [('Albir','5/05/2012','75kg'), ('Ginola','7/09/2000','57kg'), ('Ryan','16/08/1995', '69kg'), ('Eeshal','25/03/1990', '85kg')]

for x in student_data:
    students_name = (x[0])
    students_dob = x[1]
    students_weight = int(x[2][:-2])
    print(f'Name: {students_name}, Date of Birth: {students_dob}, Weight: {students_weight}kg')

#-------------------------------------------------------
# 2nd Method:

students_data_name = list(map(lambda x: x[0], student_data))
students_data_dob = list(map(lambda x: x[1], student_data))
students_data_weight = list(map(lambda x: int(x[2][:-2]), student_data))

print('students name',students_data_name)
print('students date of birth', students_data_dob)
print('students weight', students_data_weight)