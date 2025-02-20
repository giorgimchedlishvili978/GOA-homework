def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "Yes"
    else:
        return "No"

years = [2100, 2104, 2400]
for year in years:
    print(f"{year} - {is_leap_year(year)}")

# ბონუსი
def closest_leap_year(year):
    if is_leap_year(year) == "No":
        before = year - 1
        after = year + 1
        while not is_leap_year(before) == "Yes":
            before -= 1
        while not is_leap_year(after) == "Yes":
            after += 1
        if year - before <= after - year:
            return before
        else:
            return after
    return None

for year in years:
    if is_leap_year(year) == "No":
        print(f"Closest leap year to {year} is {closest_leap_year(year)}.")
