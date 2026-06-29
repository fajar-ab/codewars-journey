# Rank  : 8 kyu
# Title : For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
# Link  : https://www.codewars.com/kata/582dafb611d576b745000b74


def quote(fighter):
    return {
        "george saint pierre": "I am not impressed by your performance.",
        "conor mcgregor": "I'd like to take this chance to apologize.. To absolutely NOBODY!",
    }.get(fighter.lower())
