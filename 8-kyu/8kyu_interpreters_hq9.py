# Rank  : 8 kyu
# Title : 8kyu interpreters: HQ9+
# Link  : https://www.codewars.com/kata/591588d49f4056e13f000001


def lyrics_of_99_bottles_of_beer():
    lyrics = ""
    for number in range(99, 1, -1):
        lyrics += (
            f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
            f"Take one down and pass it around, {number - 1} "
            f"{'bottle' if number - 1 == 1 else 'bottles'} of beer on the wall.\n"
        )
    else:
        lyrics += (
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take one down and pass it around, no more bottles of beer on the wall.\n"
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall."
        )
    return lyrics


def HQ9(code):
    match code:
        case "H":
            return "Hello World!"
        case "Q":
            return code
        case "9":
            # 🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🍺🤮😵‍💫😵‍💫
            return lyrics_of_99_bottles_of_beer()


print(HQ9("9"))
