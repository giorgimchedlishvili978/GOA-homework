# მომხმარებლისგან ორი რიცხვის მიღება
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

# მომხმარებლისგან ოპერაციის არჩევა
operation = input("არჩევა ოპერაცია (დამატება - '+' / გამოკლება - '-'): ")

# ოპერაციის შესრულება
if operation == '+':
    result = num1 + num2
    print(f"შედეგი: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"შედეგი: {num1} - {num2} = {result}")
else:
    print("არასწორი ოპერაცია, გთხოვთ აირჩიოთ '+' ან '-'")
