


def get_max_per_game(filename: str) -> dict:
    """
    Returns a dictionary mapping each game to  a dict of maximum n of colors drawn.
    """
    game_map: dict[int, dict[str, int]] = {}
    with open(filename) as file:
        games: list[str] = file.read().splitlines()

    for game_data in games:
        game_id = game_data.split(':')
        game_data = game_id[1].strip()
        game_id = int(game_id[0].split(' ')[1])

        draws = game_data.split(';')
        game_map[game_id] = {}
        for draw in draws:
            n_colors = draw.split(',')
            for n_color in n_colors:
                n, color = n_color.strip().split(' ')
                n = int(n)
                game_map[game_id][color] = max(game_map[game_id].get(color, 0), n)

    return game_map


game_map = get_max_per_game("./games.txt")

#12 red cubes, 13 green cubes, and 14 blue cubes
possible_games = set()
for game_id, colors in game_map.items():
    if colors.get('red', 0) <= 12 and colors.get('green', 0) <= 13 and colors.get('blue', 0) <= 14:
        possible_games.add(game_id)

print(sum(possible_games))


# Part 2: minium number of cubes
power_sum = 0
for game_id, colors in game_map.items():
    power_sum += colors.get('red', 1) * colors.get('green', 1) * colors.get('blue', 1)

print(power_sum)
