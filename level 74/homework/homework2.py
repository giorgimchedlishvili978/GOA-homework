class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} არის {self.species}, {self.age} წლის."

# ცხოველების ობიექტების შექმნა
animal1 = Animal("მაკაკა", "ჯიმი", 5)
animal2 = Animal("პანდა", "პო", 7)
animal3 = Animal("ლომი", "ჯერი", 3)

print(animal1)
print(animal2)
print(animal3)
