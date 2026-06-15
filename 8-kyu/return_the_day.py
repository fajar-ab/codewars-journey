# Rank  : 8 kyu
# Title : Return the day
# Link  : https://www.codewars.com/kata/59dd3ccdded72fc78b000b25


def whatday(num):
    day = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }

    return day.get(num, "Wrong, please enter a number between 1 and 7")
