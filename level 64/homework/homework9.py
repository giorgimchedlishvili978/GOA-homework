def should_run_outside(weather_dry, sports_shoes_available, friend_ready):
    """
    განსაზღვრავს, თუ უნდა გავიდეთ სირბილზე.
    :param weather_dry: არის თუ არა ამინდი მშრალი
    :param sports_shoes_available: ხელმისაწვდომია თუ არა სპორტული ფეხსაცმელი
    :param friend_ready: მზად არის თუ არა მეგობარი სირბილისთვის
    :return: True, თუ უნდა გავიდეთ სირბილზე
    """
    if weather_dry and sports_shoes_available or friend_ready:
        return True
    return False

# მაგალითი:
weather_dry = True
sports_shoes_available = True
friend_ready = False
print(should_run_outside(weather_dry, sports_shoes_available, friend_ready))  # True
