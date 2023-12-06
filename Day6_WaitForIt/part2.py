

with open("./input.txt") as file:
    race_duration, best_distance = file.read().splitlines()

race_duration = int(''.join(race_duration.split()[1:]))
best_distance = int(''.join(best_distance.split()[1:]))

minimal_time = None
maximal_time = None


# Find the minimal best time
for held_time in range(race_duration + 1):
    distance = held_time * (race_duration - held_time)  # The speed (== held_time)[mm / ms] * remaining ms 
    if distance > best_distance:
        minimal_time = held_time
        break

# Find the maximal best time
for held_time in range(race_duration, -1, -1):
    distance = held_time * (race_duration - held_time)  # The speed (== held_time)[mm / ms] * remaining ms 
    if distance > best_distance:
        maximal_time = held_time
        break


print("Number of ways to beat the best", maximal_time - minimal_time + 1)  # Number of ways
