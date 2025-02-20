class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# მანქანების ობიექტების შექმნა
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2023)

print(car1)
print(car2)
print(car3)
