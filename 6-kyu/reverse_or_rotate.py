# Rank  : 6 kyu
# Title : Reverse or rotate?
# Link  : https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991


def rev_rot(strng, sz):
    if not strng or sz <= 0 or sz > len(strng):
        return ""

    result = []
    for i in range(0, len(strng), sz):
        chunk = [*strng[i : i + sz]]
        if len(chunk) == sz:
            if sum(map(int, chunk)) % 2 == 0:
                result.extend(chunk[::-1])
            else:
                chunk.append(chunk.pop(0))
                result.extend(chunk)

    return "".join(result)


print(rev_rot("733049910872815764", 5))
