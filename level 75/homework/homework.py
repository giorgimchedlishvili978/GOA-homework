class Car:
    def __init__(self, brand, model, year, engineVolume):
        self.brand = brand
        self.model = model
        self.year = year
        self.engineVolume = engineVolume

    def full_description(self):
        return f"{self.brand} {self.model}, {self.year}, {self.engineVolume}L"

# მაგალითი:
car = Car("Toyota", "Prius", 2018, 1.8)
print(car.full_description())  # "Toyota Prius, 2018, 1.8L"
