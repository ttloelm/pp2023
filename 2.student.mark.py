#Student Mark Management
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
        mark = input(f"- Student {student.name} mark: ")
        course.mark[student.id] = mark
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
