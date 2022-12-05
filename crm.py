class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, grade, address):
        super().__init__(name, age)
        self.grade = grade
        self.address = address

    def greet(self):
        print(f"My name is {self.name} and I am at the {self.grade}th grade, I live at {self.address}")


class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def greet(self):
        print(f"My name is {self.name} and I will teach {self.subject}, I have {self.experience} teaching experience")


def reg_choice():
    database_of_teachers = []
    database_of_pupil = []
    choice = input("Register as a teacher or student?").lower()
    if choice == "teacher":
        teacher = Teacher(input("Teacher's name: "), int(input("Teacher's age: ")), input("subject: "), input("Work experience: "))
        teacher.greet()
    elif choice == "student":
        student = Student(input("Student's name: "), int(input("Student's age: ")), int(input("Student's grade: ")), input("Student's address: "))
        student.greet()

reg_choice()
