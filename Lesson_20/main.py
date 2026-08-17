from database import engine, SessionLocal, Base
from models import Student, Course


# Створюємо таблиці
Base.metadata.create_all(engine)

# Підключаємося до бази даних
session = SessionLocal()


# 1. Створюємо 5 курсів

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


# 2. Створюємо 20 студентів

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


# 3. Розподіляємо студентів по курсах

students[0].courses.append(courses[0])
students[0].courses.append(courses[1])

students[1].courses.append(courses[0])
students[1].courses.append(courses[2])

students[2].courses.append(courses[1])
students[2].courses.append(courses[3])

students[3].courses.append(courses[0])
students[3].courses.append(courses[4])

students[4].courses.append(courses[2])
students[4].courses.append(courses[3])

students[5].courses.append(courses[0])
students[5].courses.append(courses[4])

students[6].courses.append(courses[1])
students[6].courses.append(courses[2])

students[7].courses.append(courses[3])
students[7].courses.append(courses[4])

students[8].courses.append(courses[0])
students[8].courses.append(courses[2])

students[9].courses.append(courses[1])
students[9].courses.append(courses[4])

students[10].courses.append(courses[0])
students[11].courses.append(courses[1])
students[12].courses.append(courses[2])
students[13].courses.append(courses[3])
students[14].courses.append(courses[4])
students[15].courses.append(courses[0])
students[16].courses.append(courses[1])
students[17].courses.append(courses[2])
students[18].courses.append(courses[3])
students[19].courses.append(courses[4])

session.commit()

print("Студентів розподілено по курсах")


# 4. Додаємо нового студента

new_student = Student(
    name="Lana",
    email="lana@gmail.com"
)

# Додаємо студента на курс Python
new_student.courses.append(courses[0])

session.add(new_student)
session.commit()

print("Нового студента додано")


# 5. Виводимо студентів курсу Python

course = session.query(Course).filter_by(name="Python").first()

print("\nСтуденти курсу Python:")

for student in course.students:
    print(student.name)


# 6. Виводимо курси студентки Anna

student = session.query(Student).filter_by(name="Anna").first()

print("\nКурси студентки Anna:")

for course in student.courses:
    print(course.name)


# 7. Оновлюємо дані студента

student = session.query(Student).filter_by(name="John").first()

student.name = "John Updated"

session.commit()

print("\nДані студента оновлено")


# 8. Оновлюємо назву курсу

course = session.query(Course).filter_by(name="Java").first()

course.name = "Advanced Java"

session.commit()

print("Назву курсу оновлено")


# 9. Видаляємо студента

student = session.query(Student).filter_by(name="Michael").first()

session.delete(student)
session.commit()

print("Студента Michael видалено")


# Закриваємо з'єднання з базою даних
session.close()