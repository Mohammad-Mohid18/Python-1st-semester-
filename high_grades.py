# Python program to filter students by high grades


students = [
    {'name': 'John', 'grade': 90},
    {'name': 'Jane', 'grade': 97},
    {'name': 'Mike', 'grade': 95},
    {'name': 'Emily', 'grade': 80}
]

def extract(a):
    return a['grade'] >= 95

result = filter(extract, students)
print(list(result))
