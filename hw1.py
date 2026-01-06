class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def descride(self):
        return f"Студент {self.name}, возраст {self.age}, средний балл {self.grade} "

    def improve_grade(self, points):
        self.grade += points

student1 = Student("kan" , 21, 85)
student2 = Student("Бек", 20, 65)

print(student1.descride())
student1.improve_grade(5)
print(student1.descride())
print(student2.descride())
student2.improve_grade(3)
print(student2.descride())