from contextlib import suppress


def is_adjacent_to_star(data: list[list[str]], row: int, column: int) -> tuple[int, int]:
    """
    Returns the (row, column) of star that the number at (row, column) is adjacent to,
    or False if it is not adjacent
    """
    for roff in range(-1, 2):
        for coff in range(-1, 2):
            with suppress(IndexError):
                c = data[row + roff][column + coff]
                if not c.isnumeric()  and c == '*':
                    return (row + roff, column + coff)

    return False


with open("./schematic.txt") as file:
    fdata: list[list[str]] = file.read().splitlines()


nbuffer = []
sum_gears = 0
gear_to_numbers = {}  # Maps gear position to adjacent numbers
was_adjacent = False

for row in range(len(fdata)):
    for column in range(len(fdata[0])):
        char = fdata[row][column]
        if char.isnumeric():
            nbuffer.append(char)
            if star_pos := is_adjacent_to_star(fdata, row, column):
                was_adjacent = True
                adjacent_star_pos = star_pos

        elif nbuffer:
            if was_adjacent:
                new_num = int(''.join(nbuffer))
                # Create a map that maps the star position to it's numbers and add the number
                # to the correct key
                gear_to_numbers[adjacent_star_pos] = gear_to_numbers.get(adjacent_star_pos, [])
                gear_to_numbers[adjacent_star_pos].append(new_num)
                was_adjacent = False

            nbuffer.clear()


for gear, numbers in gear_to_numbers.items():
    if len(numbers) == 1:
        continue

    sum_gears += numbers[0] * numbers[1]

print(sum_gears)
