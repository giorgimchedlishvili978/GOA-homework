def should_watch_football(is_saturday_or_sunday, no_other_activities, favorite_team_playing):
    """
    განსაზღვრავს, თუ უნდა ვუყუროთ ფეხბურთს.
    :param is_saturday_or_sunday: არის თუ არა დღე შაბათი ან კვირა
    :param no_other_activities: არ გვაქვს სხვა საქმეები
    :param favorite_team_playing: თუ ჩვენი საყვარელი გუნდი თამაშობს
    :return: True, თუ უნდა ვუყუროთ ფეხბურთს
    """
    if (is_saturday_or_sunday and no_other_activities) or favorite_team_playing:
        return True
    return False

# მაგალითი:
is_saturday_or_sunday = True
no_other_activities = True
favorite_team_playing = False
print(should_watch_football(is_saturday_or_sunday, no_other_activities, favorite_team_playing))  # True
