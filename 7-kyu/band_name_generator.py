# Rank  : 7 kyu
# Title : Band name generator
# Link  : https://www.codewars.com/kata/59727ff285281a44e3000011


def band_name_generator(name):
    letter = name[0]

    if name.startswith(letter) and name.endswith(letter):
        new_band = name + name[1:]
        return new_band.capitalize()

    return f"The {name.capitalize()}"
