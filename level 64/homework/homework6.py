def should_sleep(late_time, tired, need_to_get_up_early, lights_off):
    """
    განსაზღვრავს, თუ უნდა დავიძინოთ.
    :param late_time: არის თუ არა დრო გვიანი
    :param tired: არის თუ არა ადამიანი დაღლილი
    :param need_to_get_up_early: საჭიროა თუ არა ადრიანად ადგომა მეორე დღეს
    :param lights_off: არის თუ არა შუქი გამორთული
    :return: True, თუ უნდა დავიძინოთ
    """
    if late_time and tired or need_to_get_up_early and lights_off:
        return True
    return False

# მაგალითი:
late_time = True
tired = True
need_to_get_up_early = False
lights_off = True
print(should_sleep(late_time, tired, need_to_get_up_early, lights_off))  # True
