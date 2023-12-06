




with open("./input.txt") as file:
    race_durations, best_distances = file.read().splitlines()

race_durations = map(int, race_durations.split()[1:])
best_distances = map(int, best_distances.split()[1:])
races = list(zip(race_durations, best_distances))

n_ways_multiplied = 1
for duration, best_distance in races:
    n_ways_race = 0
    for held_time in range(duration + 1):
        distance = held_time * (duration - held_time)  # The speed (== held_time)[mm / ms] * remaining ms 
        if distance > best_distance:
            n_ways_race += 1

    n_ways_multiplied *= n_ways_race


print("Multiplied number of ways per race", n_ways_multiplied)