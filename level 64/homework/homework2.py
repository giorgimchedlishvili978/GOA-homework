def can_go_out(weather_good, enough_time, ready_to_go):
    """
    განსაზღვრავს, თუ შეგვიძლია გავიდეთ გარეთ.
    :param weather_good: არის თუ არა ამინდი კარგი
    :param enough_time: გვაქვს თუ არა საკმარისი დრო
    :param ready_to_go: მზად ვართ თუ არა გასასვლელად
    :return: True, თუ შესაძლებელია გასვლა გარეთ
    """
    if weather_good or enough_time:
        return ready_to_go
    return False

# მაგალითი:
weather_good = True
enough_time = False
ready_to_go = True
print(can_go_out(weather_good, enough_time, ready_to_go))  # True
