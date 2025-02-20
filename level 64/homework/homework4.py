def should_take_item(item_available, item_allowed, other_person_wants):
    """
    განსაზღვრავს, თუ უნდა ავიღოთ ნივთი.
    :param item_available: არის თუ არა ნივთი ხელმისაწვდომი
    :param item_allowed: არის თუ არა ნივთის წაღება დაშვებული
    :param other_person_wants: სურს თუ არა სხვა ადამიანს ნივთის გამოყენება
    :return: True, თუ შეიძლება ავიღოთ ნივთი
    """
    if item_available and item_allowed and not other_person_wants:
        return True
    return False

# მაგალითი:
item_available = True
item_allowed = True
other_person_wants = False
print(should_take_item(item_available, item_allowed, other_person_wants))  # True
