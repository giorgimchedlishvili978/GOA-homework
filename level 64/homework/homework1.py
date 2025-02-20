def test_passed(grades, pass_threshold=60, authors=None):
    """
    ამოწმებს, თუ რომელიმე შეფასება აკმაყოფილებს მოთხოვნებს.
    :param grades: სიითი შეფასებები
    :param pass_threshold: მინიმალური გამვლელი შეფასება
    :param authors: შესაძლოა, დამწერების სიაც, რომლებიც გავლენას მოახდენენ
    :return: True, თუ ერთ-ერთი შეფასება ამოწმებს მოთხოვნებს
    """
    for grade in grades:
        if grade >= pass_threshold:
            return True
    return False

# მაგალითი:
grades = [55, 65, 45]  # შეფასებები
print(test_passed(grades))  # True
