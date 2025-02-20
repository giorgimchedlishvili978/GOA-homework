class Person:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
    
    def __str__(self):
        return f"ადამიანი:\nსახელი: {self.name},\nასაკი: {self.age},\nსიმაღლე: {self.height},\nსქესი: {self.gender}"

# ობიექტების სია
people = [
    Person("ნინო", 25, 170, "ქალი"),
    Person("გიორგი", 30, 180, "კაცი"),
    Person("ანა", 22, 160, "ქალი"),
    Person("ლევან", 35, 175, "კაცი")
]

# თითოეული ადამიანის მონაცემების ამოღება
for person in people:
    print(person)
    print()  # ახალი ხაზის დამატება
