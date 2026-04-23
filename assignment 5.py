marks = [56, 78, 93, 42, 97, 85, 34, 67, 73, 86]
passed = [mark for mark in marks if mark >= 50]
print("The marks above 50 are:", passed)


num_students = int(input("Enter the number of students: "))
marks = []
for i in range(num_students):
    mark = int(input("Enter the mark of student (" + str(i + 1) + "): "))
    marks.append(mark)
print("The highest mark is:", max(marks))
print("The lowest mark is:", min(marks))


values = []
for i in range(10):
    num = int(input("Enter a number: "))
    values.append(num)
print("List before sorting:", values)
values.sort(reverse=True)
print("List after sorting:", values)
print("Highest three items:", values[:3])


size1 = int(input("Enter the number of students registered in Group(A): "))
list1 = []
for i in range(size1):
    mark = int(input("Student (" + str(i + 1) + "): "))
    list1.append(mark)
size2 = int(input("Enter the number of students registered in Group(B): "))
list2 = []
for i in range(size2):
    mark = int(input("Student (" + str(i + 1) + "): "))
    list2.append(mark)
combined = list1 + list2
print("The concatenated grades:", combined)


num_students = int(input("Enter the number of students: "))
marks = []
for i in range(num_students):
    mark = int(input("Student (" + str(i + 1) + "): "))
    marks.append(mark)
average = sum(marks) / num_students
above_avg = sum(1 for mark in marks if mark > average)
failed = sum(1 for mark in marks if mark < 50)
print("The average is:", average)
print("The number of students above average is:", above_avg)
print("The number of students who failed is:", failed)


exam1 = []
exam2 = []
max_grades = []
for i in range(5):
    mark1 = int(input("Enter the marks of student (" + str(i + 1) + ") Exam(1): "))
    mark2 = int(input("Enter the marks of student (" + str(i + 1) + ") Exam(2): "))
    exam1.append(mark1)
    exam2.append(mark2)
    max_grades.append(max(mark1, mark2))
print("\nExam1\tExam2\tMaximum")
for i in range(5):
    print(exam1[i], "\t", exam2[i], "\t", max_grades[i])