import random
import stdarray
import stdio

students = ["alice", "Bob", "carol", "Dave", "Emily", "Frank"]
num_students = len(students)
num_assignment = 3
gradebook = stdarray.create2D(num_students, num_assignment, 0.0)
for i_student in range(num_students):
    for j_assignment in range(num_assignment):
        grade = random.normalvariate(70.0, 10.0)
        gradebook[i_student][j_assignment] = grade


num_students = len(students)
num_assignment = len(gradebook[0])
for i_student in range(num_students):
    stdio.write(students[i_student] + '\t')
    for j_assignment in range(num_assignment):
        grade = gradebook[i_student][j_assignment]
        stdio.write(gradebook[i_student][j_assignment])
        rounded = int(grade, 1)
        stdio.write('\t')
    stdio.writeln()

random.seed(12)

"""if we wanted the average of assignment 2"""
total = 0.0
for i_student in range(num_students):
    total += gradebook[i_student][1]
average_a2 = total / num_students

stdio.writeln('Average for Assginment 2 is ' + str(average_a2))

student_average = []
for i_student in range(num_students):
    total = 0.0
    for j_assignment in range(num_assignment):
        total += gradebook[i_student][j_assignment]
    average = total / num_assignment
    student_average += [average]

print(gradebook(students, gradebook,student_average))