#-------------------------------------------------------
# Students Grades Tracker
#-------------------------------------------------------
# Dictionary:

grades_track = {
    'mohid' : 20,
    'asad' : 24,
    'zoraz' : 21,
    'ali' : 23,
    'aoun' : 25,
    'albir' : 28,
    'faiez' : 27,
    'shahzor' : 23
}

#-------------------------------------------------------
#1
def add(name,grade):
    if name in grades_track:
        print('Student already exists')
    else:
        grades_track[name] = grade
        print('Student added successfully')

#-------------------------------------------------------
#2
def update(name,grade):
    if name in grades_track:
        grades_track[name] = grade
        print('Grade updated successfully')
    else:
        print('Student not found')

#-------------------------------------------------------
#3
def delete(name):
    if name in grades_track:
        del grades_track[name]
        print('Student deleted successfully')
    else:
        print('Student not found')

#-------------------------------------------------------
#4
def display():
    for name, grade in grades_track.items():
        print(f'{name}: {grade}')

#-------------------------------------------------------
#5
def average():
    total = sum(grades_track.values())
    count = len(grades_track)
    return total / count

#-------------------------------------------------------
#6
def highest_grade():
    y = 0
    h = None
    for name,x  in grades_track.items():
        if x > y:
            y = x
            h = name
    print('highest grades  are',y,'achieved by',h)

#-------------------------------------------------------
#7
def lowest_grade():
    y = float('inf')
    h = None
    for name,x  in grades_track.items():
        if x < y:
            y = x
            h = name
    print('lowest grades  are',y,'achieved by',h)

#-------------------------------------------------------
#8
def search(name):
    if name in grades_track:
        print(f'{name} has a grade of {grades_track[name]}')
    else:
        print('Student not found')

#-------------------------------------------------------

while True:
    choose = int(input('choose your command(1 = add),(2 = updating grade),(3 = removing name),(4 = display),(5 = avg),(6 = max num),(7 = min num),(8 = searching),(9 = exit)'))
    if choose == 9:
        break
    elif choose == 1:
        name = input('Enter student name: ')
        grade = int(input('Enter student grade: '))
        add(name, grade)
    elif choose == 2:
        name = input('Enter student name: ')
        grade = int(input('Enter updated student grade: '))
        update(name, grade)
    elif choose == 3:
        name = input('Enter student name: ')
        delete(name)
    elif choose == 4:
        display()
    elif choose == 5:
        print('Average grade is', average())
    elif choose == 6:
        highest_grade()
    elif choose == 7:
        lowest_grade()
    elif choose == 8:
        name = input('Enter student name: ')
        search(name)
    else:
        print('Invalid command')

#-------------------------------------------------------