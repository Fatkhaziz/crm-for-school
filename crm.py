class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, grade, address):
        super().__init__(name, age)
        self.grade = grade
        self.address = address


class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience


def reg_choice():
    database_of_teachers = []
    database_of_pupil = []
    choice = input("Register as a teacher or student?").lower()
    if choice == "teacher":
        teacher = Teacher(input("Teacher's name: "), int(input("Teacher's age: ")), input("subject: "), input("Work experience: "))
        # print("Name:", teacher.name)
        # print("Age:", teacher.age, 'years old')
        # print("subject:", teacher.subject)
        # print(teacher.experience, "years of teaching experience")
        print(f"My name is {teacher.name} and I will teach {teacher.subject}, I have {teacher.experience} teaching experience")
    #     can be done either way
    elif choice == "student":
        student = Student(input("Student's name: "), int(input("Student's age: ")), int(input("Student's grade: ")), input("Student's address: "))
        print("Name:", student.name)
        print(student.age, "years old")
        print(f"currently at the {student.grade}'s grade")
        print("Lives at:", student.address)
        # print(f"My name is {student.name} and I am at the {student.grade}th grade, I live at {student.address}")

reg_choice()
