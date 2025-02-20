def should_recall_information(task_urgent, info_needed, time_available):
    """
    განსაზღვრავს, თუ უნდა გავიხსენოთ ინფორმაცია.
    :param task_urgent: არის თუ არა დავალება აქტუალური
    :param info_needed: არის თუ არა ინფორმაცია საჭირო
    :param time_available: გვაქვს თუ არა დრო დასამუშავებლად
    :return: True, თუ უნდა გავიხსენოთ ინფორმაცია
    """
    if task_urgent and info_needed and time_available:
        return True
    return False

# მაგალითი:
task_urgent = True
info_needed = True
time_available = True
print(should_recall_information(task_urgent, info_needed, time_available))  # True
