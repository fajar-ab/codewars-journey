# Rank  : 7 kyu
# Title : Split In Parts
# Link  : https://www.codewars.com/kata/5650ab06d11d675371000003


def split_in_parts(s, part_length):
    return " ".join(part_length[i : i + s] for i in range(0, len(part_length), s))
