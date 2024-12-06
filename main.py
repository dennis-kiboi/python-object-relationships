# one-to-many relationship
# one teacher has many students
# a student belongs to a teacher

# one way one-to-many relationship
# two way one-to-many relationship
class Teacher:
    def __init__(self, name):
        self.name = name
        # self.students = []

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        # self.students.append(student)
        student.teacher = self # Assign a teacher to this student

    def __repr__(self):
        return f"Teacher({self.name})"
    
class Student:
    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.teacher = None # Reference to a Teacher
        Student.all.append(self)

    def enroll_in_course(self, course):
        Enrollment(self, course)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.teacher})"
    
class Course:
    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enroll_student(self, student):
        Enrollment(student, self)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]
    
    def __repr__(self):
        return f"Course({self.title})"
    
class Enrollment:
    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        Enrollment.all.append(self)

    def __repr__(self):
        return f"Enrollment({self.student.name}, {self.course.title})"

    
# Create teacher and student instances
teacher1 = Teacher("Mrs. Smith")
teacher2 = Teacher("Mr. Kimani")
teacher3 = Teacher("Ms. Patel")

student1 = Student("John Doe", 20)
student2 = Student("Jane Wanjiku", 18)
student3 = Student("Alice Johnson", 21)
student4 = Student("David Mwangi", 19)
student5 = Student("Emily Kimani", 17)
student6 = Student("Frank Otieno", 22)

# Assign students to teachers (deterministic assignment)
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher2.add_student(student3)
teacher2.add_student(student4)
teacher3.add_student(student5)
teacher3.add_student(student6)

# Create courses
course1 = Course("Digital Electronics")
course2 = Course("Operating Systems")
course3 = Course("Data Structures and Algorithms")

# Enroll students to a course
student5.enroll_in_course(course1)
student5.enroll_in_course(course3)

course2.enroll_student(student6) # student6, course2
course3.enroll_student(student6) # student6, course3

print(student5.courses())
print(course3.students())