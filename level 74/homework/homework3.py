class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name} არის {self.age} წლის და სწავლობს {self.grade} კლასში."

# მოსწავლეების ობიექტების შექმნა
student1 = Student("ნიკა", 15, 9)
student2 = Student("მარიკა", 14, 8)
student3 = Student("გიორგი", 16, 10)

print(student1)
print(student2)
print(student3)
