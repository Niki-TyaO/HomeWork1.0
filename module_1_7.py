grades = [[5,3,4,5,4], [4,3,4,5,3,4],[5,4,5]]
students = {'Vasya', 'Petya', 'Katya'}
students = list(students)
grades_new = [sum(grades[0]), sum(grades[1]), sum(grades[2])]
grades_new1 = [len(grades[0]), len(grades[1]), len(grades[2])]
grades_end = grades_new[0]/grades_new1[0], grades_new[1]/grades_new1[1], grades_new[2]/grades_new1[2]
Dict = dict(zip(students, grades_end))
print(Dict)