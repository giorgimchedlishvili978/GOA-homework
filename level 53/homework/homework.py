import math

def count_area(shape, *dimensions):
    if shape == "rectangle" and len(dimensions) == 2:
        length, width = dimensions
        return length * width
    elif shape == "circle" and len(dimensions) == 1:
        radius = dimensions[0]
        return math.pi * radius * radius
    
    elif shape == "triangle" and len(dimensions) == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    else:
        return "Invalid input or shape"

print(count_area("rectangle", 5, 10))   # 50
print(count_area("circle", 7))          # 153.93804002589985
print(count_area("triangle", 3, 4, 5))  # 6.0
