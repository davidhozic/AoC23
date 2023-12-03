from contextlib import suppress


def is_adjacent_to_char(data: list[list[str]], row: int, column: int):
    for roff in range(-1, 2):
        for coff in range(-1, 2):
            with suppress(IndexError):
                c = data[row + roff][column + coff]
                if not c.isnumeric()  and c != '.':
                    return True

    return False


sum_adjacent = 0
with open("./schematic.txt") as file:
    fdata: list[list[str]] = file.read().splitlines()


nbuffer = []
was_adjecent = False
for row in range(len(fdata)):
    for column in range(len(fdata[0])):
        # Iterate through all rows and columns
        char = fdata[row][column]
        # If the character is part of the entire number, check if it adjacent to
        # a non '.' character and remember the adjacent status until entire number has been parsed.
        # Then add that to the sum.
        if char.isnumeric():
            nbuffer.append(char)
            if is_adjacent_to_char(fdata, row, column):
                was_adjecent = True

        else:
            if was_adjecent:
                was_adjecent = False
                sum_adjacent += int(''.join(nbuffer))

            nbuffer.clear()


print(sum_adjacent)
