#Student Mark Management
import math
import numpy as np
import curses
grading_scale = {"20" : 4, "18" : 4, "16" : 3.7, "14" : 3.3, "12" : 3.0, "10" : 2.7, "8" : 2.3, "6" : 2.0, "4" : 1.7, "2" : 1.3, "0" : 0,}
credit = []
mark = []
class Student:
    def __init__(self, name, dob, id):
        self.__name = name
        self.__dob = dob
        self.__id = id
    def __str__(self):
        return f"Student {self.name}: {self.id} {self.dob}"
    @property
    def name(self):
        return self.__name
    @property
    def dob(self):
        return self.__dob
    @property
    def id(self):
        return self.__id
class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.mark = {}
    def __str__(self):
        return f"Course {self.name}: {self.id}"
    def show_marks(self, students):
        print(f"Course {self.name}:")
        for student in students:
            print(f"- Student {student.name}: {self.mark[student.id]}")
#enter student infos
students = []
no_students = int(input("Enter number of students: "))
for i in range(no_students):
    name = input("Enter student name: ")
    dob = input("Enter student dob: ")
    id = input("Enter student id: ")
    students += [Student(name, dob, id)]
#enter course infos
courses = []
no_courses = int(input("Enter number of courses: "))
for i in range(no_courses):
    name = input("Enter course name: ")
    id = input("Enter course id: ")
    courses += [Course(name, id)]
#enter course marks
for course in courses:
    print(f"Enter mark for course {course.name} ")
    for student in students:
        mark = float (input(f"- Student {student.name} mark: "))
        course.mark[student.id] = mark
#enter course credits
for course in courses:
    credit = float (input(f"Enter credit for course {course.name}: "))
    course.credit = credit
#rounding marks to 1 decimal place
for course in courses:
    for student in students:
        course.mark[student.id] = math.floor(course.mark[student.id] * 10) / 10
#calculate the gpa of each student
for student in students:
    total_credit = sum(course.credit for course in courses)
    GPA = 0
    for course in courses:
        GPA += (course.mark[student.id] * 0.2 * course.credit) / total_credit
    GPA = math.floor(GPA * 10) / 10
    student.GPA = GPA
#sort students by GPA
students.sort(key=lambda student: student.GPA, reverse=True)
#listing functions
def list_courses(courses):
    for course in courses:
        print(course)
def list_students(students):
    for student in students:
        print(student)
#main
print("Listing students:")
list_students(students)
print("Listing courses:")
list_courses(courses)
print("Listing course marks:")
for course in courses:
    course.show_marks(students)
print("Listing student GPA:")
for student in students:
    print(f"- Student {student.name}: {student.GPA}")
print("Listing students by GPA:")
list_students(students)



