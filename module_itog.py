def calculate_average_grade():
    average_grades = {}

    for a in range(len(grades)):
        student_grade = sum(grades[a]) / len(grades[a])
        average_grades[list(students)[a]] = student_grade

    return average_grades


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = calculate_average_grade()
print(average_grades)