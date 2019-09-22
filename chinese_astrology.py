"""
Determine the entered year in Chinese astrology.
"""


def what_year(year):
    """
    Find out information about a year.
    :param year: A year
    :return: Information about a year
    """
    year = int(year)
    if year < 1:
        raise ValueError("A year must be more than 0!")

    colors = ("white", "blue", "green", "red", "yellow")
    elements = ("Metal", "Water", "Wood", "Fire", "Earth")
    animals = (
        "monkey",
        "rooster",
        "dog",
        "pig",
        "rat",
        "ox",
        "tiger",
        "rabbit",
        "dragon",
        "snake",
        "horse",
        "goat"
    )

    y = (year % 60 % 10) // 2

    return "%d is the %s %s year. An element is %s." % (
        year,
        colors[y],
        animals[year % 12],
        elements[y],
    )
