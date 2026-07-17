# Rank  : 8 kyu
# Title : Crash Override
# Link  : https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f

from ast import alias

FIRST_NAME = {
    "A": "Alpha",
    "B": "Beta",
    "C": "Cache",
    "D": "Data",
    "E": "Energy",
    "F": "Function",
    "G": "Glitch",
    "H": "Half-life",
    "I": "Ice",
    "J": "Java",
    "K": "Keystroke",
    "L": "Logic",
    "M": "Malware",
    "N": "Nagware",
    "O": "OS",
    "P": "Phishing",
    "Q": "Quantum",
    "R": "RAD",
    "S": "Strike",
    "T": "Trojan",
    "U": "Ultraviolet",
    "V": "Vanilla",
    "W": "WiFi",
    "X": "Xerox",
    "Y": "Y",
    "Z": "Zero",
}
SURNAME = {
    "A": "Analogue",
    "B": "Bomb",
    "C": "Catalyst",
    "D": "Discharge",
    "E": "Electron",
    "F": "Faraday",
    "G": "Gig",
    "H": "Hacker",
    "I": "IP",
    "J": "Jabber",
    "K": "Killer",
    "L": "Lazer",
    "M": "Mike",
    "N": "n00b",
    "O": "Overclock",
    "P": "Payload",
    "Q": "Quark",
    "R": "Roy",
    "S": "Spy",
    "T": "T-Rex",
    "U": "Unit",
    "V": "Virus",
    "W": "Worm",
    "X": "X",
    "Y": "Yob",
    "Z": "Zombie",
}


def alias_gen(f_name: str, l_name: str) -> str:
    f = f_name[0].upper()
    l = l_name[0].upper()

    if not (f + l).isalpha():
        return "Your name must start with a letter from A - Z."

    return FIRST_NAME[f] + " " + SURNAME[l]
