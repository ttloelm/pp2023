#Student mark management

#enter student infos
def enter_student_info():
    name = input("Enter student name: ")
    dob = input("Enter student dob: ")
    id = input("Enter student id: ")
    return {
        "name": name,
        "dob": dob,
        "id": id
    }
#enter course infos
def enter_course_info():
    name = input("Enter course name: ")
    id = input("Enter course id: ")
    return {
        "name": name,
        "id": id
    }

def input_mark(course, students):
    print(f"Enter mark for course {course['name']} ")
    course['mark'] = {}
    for student in students:
        mark = input(f"- Student {student['name']} mark: ")
        course['mark'][student['id']] = mark
#listing functions
#enter student infos
students = []
no_students = int(input("Enter number of students: "))
for i in range(no_students):
    students += [enter_student_info()]
#enter course infos
courses = []
no_courses = int(input("Enter number of courses: "))
for i in range(no_courses):
    courses += [enter_course_info()]

def list_courses(courses):
    for course in courses:
        print(f"Course {course['name']}: {course['id']}")
def list_students(students):
   for student in students:
       print(f"Student {student['name']}: {student['id'] + ' ' + student['dob']}")
def show_course_marks(course, students):
    print(f"Course {course['name']}:")
    for student in students:
        print(f"- Student {student['name']}: {course['mark'][student['id']]}")
#main


#enter course marks
for course in courses:
    input_mark(course, students)

print("Listing students:")
list_students(students)
print("Listing courses:")
list_courses(courses)
print("Listing course marks:")
for course in courses:
    show_course_marks(course, students)








    
