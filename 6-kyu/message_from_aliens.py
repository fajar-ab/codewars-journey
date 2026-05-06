# Rank  : 6 kyu
# Title : Message from Aliens
# Link  : https://www.codewars.com/kata/reviews/59b776d96d9dec3ce40017aa/groups/69fadf4ac92d1732dbfb3a21

def decode(message):
    patterns = {
        '__':   ' ',
        '/\\':  'a',
        ']3':   'b',
        '(':    'c',
        '|)':   'd',
        '[-':   'e',
        '/=':   'f',
        '(_,':  'g',
        '|-|':  'h',
        '|':    'i',
        '_T':   'j',
        '/<':   'k',
        '|_':   'l',
        '|\\/|':'m',
        '|\\|': 'n',
        '()':   'o',
        '|^':   'p',
        '()_':  'q',
        '/?':   'r',
        '_\\~': 's',
        '~|~':  't',
        '|_|':  'u',
        '\\/':  'v',
        '\\/\\/':'w',
        '><':   'x',
        '`/':   'y',
        '~/_':  'z'
    }

    separator = message[0]
    alien_message = [ms for ms in reversed(message.split(separator)) if ms]
    real_message = ""

    for key in alien_message:
        real_message += patterns[key]

    return real_message



