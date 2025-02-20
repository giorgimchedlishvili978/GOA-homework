def enter_text():
    previous_texts = []  # სია, სადაც შევინახავთ უკვე შეყვანილ ტექსტებს

    while True:
        user_input = input("შეიყვანეთ ტექსტი: ")
        if user_input in previous_texts:
            print("ეს ტექსტი უკვე შეიყვანეთ. სცადეთ სხვა.")
        else:
            previous_texts.append(user_input)
            print("ტექსტი წარმატებით შეიყვანეთ.")
            break
