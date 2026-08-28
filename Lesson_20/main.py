import random

from database import engine, SessionLocal, Base
from models import Student, Course



Base.metadata.create_all(engine)


session = SessionLocal()


courses = [
    Course(name="Python"),
    Course(name="SQL"),
    Course(name="Java"),
    Course(name="Web Development"),
    Course(name="QA Testing")
]

session.add_all(courses)
session.commit()

print("5 курсів створено")



students = [
    Student(name="Anna", email="anna@gmail.com"),
    Student(name="John", email="john@gmail.com"),
    Student(name="Maria", email="maria@gmail.com"),
    Student(name="David", email="david@gmail.com"),
    Student(name="Emma", email="emma@gmail.com"),
    Student(name="Daniel", email="daniel@gmail.com"),
    Student(name="Sophia", email="sophia@gmail.com"),
    Student(name="Michael", email="michael@gmail.com"),
    Student(name="Olivia", email="olivia@gmail.com"),
    Student(name="James", email="james@gmail.com"),
    Student(name="Liam", email="liam@gmail.com"),
    Student(name="Mia", email="mia@gmail.com"),
    Student(name="Noah", email="noah@gmail.com"),
    Student(name="Emily", email="emily@gmail.com"),
    Student(name="Lucas", email="lucas@gmail.com"),
    Student(name="Chloe", email="chloe@gmail.com"),
    Student(name="Ethan", email="ethan@gmail.com"),
    Student(name="Grace", email="grace@gmail.com"),
    Student(name="Alexander", email="alex@gmail.com"),
    Student(name="Sofia", email="sofia@gmail.com")
]

session.add_all(students)
session.commit()

print("20 студентів створено")



for student in students:
    random_courses = random.sample(courses, random.randint(1, 3))

    for course in random_courses:
        student.courses.append(course)

session.commit()

print("Студентів випадково розподілено по курсах")



new_student = Student(
    name="Lana",
    email="lana@gmail.com"
)


new_student.courses.append(courses[0])

session.add(new_student)
session.commit()

print("Нового студента додано")


course = session.query(Course).filter_by(name="Python").first()

print("\nСтуденти курсу Python:")

for student in course.students:
    print(student.name)



student = session.query(Student).filter_by(name="Anna").first()

print("\nКурси студентки Anna:")

for course in student.courses:
    print(course.name)


student = session.query(Student).filter_by(name="John").first()

student.name = "John Updated"

session.commit()

print("\nДані студента оновлено")


course = session.query(Course).filter_by(name="Java").first()

course.name = "Advanced Java"

session.commit()

print("Назву курсу оновлено")


student = session.query(Student).filter_by(name="Michael").first()

session.delete(student)
session.commit()

print("Студента Michael видалено")


session.close()