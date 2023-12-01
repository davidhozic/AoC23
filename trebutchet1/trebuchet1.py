"""
Advent of code solution: Trebuchet - 1st December
"""
from typing import List

# PART ONE
# total_sum = 0
# with open("codes.txt") as file:
#     data = file.read().splitlines()
#     for line in data:
#         first_c = None
#         last_c = None
#         for c in line:
#             if c.isnumeric():
#                 first_c = c
#                 break
        
#         for c in line[::-1]:
#             if c.isnumeric():
#                 last_c = c
#                 break

#         total_sum += int(first_c + last_c)

# print(total_sum)



# PART 2
total_sum = 0
valids = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def get_first_valid(i: int, line: str):
    for k in valids:
        if line[i:].startswith(k):
            return k

with open("codes.txt") as file:
    data = file.read().lower().splitlines()
    lines: List[str] = []
    for line in data:
        # Replace first worded number from the front
        for i in range(len(line)):
            if k := get_first_valid(i, line):
                len_key = len(k)
                replacement = line[i:i + len_key].replace(k, valids[k])
                line = list(line)
                line[i:len_key] = replacement
                line = ''.join(line)
                break
        
        # Replace last worded number from the front
        for i in range(len(line) - 1, -1, -1):
            if k := get_first_valid(i, line):
                len_key = len(k)
                replacement = line[i:i + len_key].replace(k, valids[k])
                line = list(line)
                line[i:len_key] = replacement
                line = ''.join(line)
                break

        lines.append(line)

    for line in lines:
        first_c = None
        last_c = None
        for c in line:
            if c.isnumeric():
                first_c = c
                break

        for c in line[::-1]:
            if c.isnumeric():
                last_c = c
                break

        total_sum += int(first_c + last_c)

print(total_sum)

