grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grade_point_average = []

for a in grades:
     b = sum(a)/len(a)
     grade_point_average.append(b)
dict1 = dict(zip(students,grade_point_average))
print(dict1)