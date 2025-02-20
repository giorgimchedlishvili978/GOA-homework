def should_go_to_party(friends_agree, no_work_next_day, party_nearby):
    """
    განსაზღვრავს, თუ უნდა წავიდეთ წვეულებაზე.
    :param friends_agree: თანახმა არიან თუ არა მეგობრები წასვლაზე
    :param no_work_next_day: არის თუ არა მეორე დღეს სამუშაო
    :param party_nearby: არის თუ არა წვეულება ახლოს
    :return: True, თუ უნდა წავიდეთ წვეულებაზე
    """
    if (friends_agree and not no_work_next_day) or party_nearby:
        return True
    return False

# მაგალითი:
friends_agree = True
no_work_next_day = False
party_nearby = False
print(should_go_to_party(friends_agree, no_work_next_day, party_nearby))  # True
