def should_stay_home(weather_rain_or_snow, no_plans_outside):
    """
    განსაზღვრავს, თუ უნდა დავრჩეთ სახლში.
    :param weather_rain_or_snow: არის თუ არა ამინდი წვიმიანი ან თოვლიანი
    :param no_plans_outside: გვაქვს თუ არა გეგმები გარეთ გასვლისთვის
    :return: True, თუ უნდა დავრჩეთ სახლში
    """
    if weather_rain_or_snow and not no_plans_outside:
        return True
    return False

# მაგალითი:
weather_rain_or_snow = True
no_plans_outside = True
print(should_stay_home(weather_rain_or_snow, no_plans_outside))  # True
