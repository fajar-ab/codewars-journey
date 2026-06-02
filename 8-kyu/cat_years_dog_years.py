# Rank  : 8 kyu
# Title : Cat years, Dog years
# Link  : https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

def human_years_cat_years_dog_years(human_years):
    cat_years = dog_years = 0

    for age in range(1, human_years+1):
        match age:
            case 1: cat_years, dog_years = cat_years + 15, dog_years + 15
            case 2: cat_years, dog_years = cat_years + 9, dog_years + 9
            case _: cat_years, dog_years = cat_years + 4, dog_years + 5

    return [human_years, cat_years, dog_years]

