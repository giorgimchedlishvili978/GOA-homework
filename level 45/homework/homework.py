def calculate(a, b):
    summation = a + b
    multiplication = a * b
    subtraction = a - b
    return summation, multiplication, subtraction


result = calculate(5, 3)
print(result)  # (8, 15, 2)

def first_character(string):
    if string:  # проверяем, что строка не пустая
        return string[0]
    return None

char = first_character("hello")
print(char)  # ''

def square(number):
    return number ** 2

# მაგალითად
result = square(4)
print(result)  # 16
