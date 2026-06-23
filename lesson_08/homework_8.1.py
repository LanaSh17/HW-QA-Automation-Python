class Student:

    def __init__(self, first_name, last_name, age, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def change_average_score(self, score):
            self.average_score = score

student_info = Student("Lana", "Shanava", 19, average_score=8)
print(student_info.first_name)
print(student_info.last_name)
print(student_info.age)
print(student_info.average_score)

student_info.change_average_score(10)
print(student_info.average_score)