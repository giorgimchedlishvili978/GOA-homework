def can_take_step(barrier, space_free, signal_coming):
    """
    განსაზღვრავს, თუ გადავდგათ ნაბიჯი.
    :param barrier: არსებობს თუ არა ბარიერი
    :param space_free: არის თუ არა სივრცე თავისუფალი
    :param signal_coming: მოდის თუ არა სიგნალი მეორე მხარიდან
    :return: True, თუ შესაძლებელია ნაბიჯის გადადგმა
    """
    if not barrier and space_free:
        return True
    if signal_coming:
        return True
    return False

# მაგალითი:
barrier = False
space_free = True
signal_coming = False
print(can_take_step(barrier, space_free, signal_coming))  # True
