import re



with open("input.txt") as file:
    fdata = file.read()


def create_mapping(map_name: str):
    """
    Creates a list of parsed tuples that contain (source_start_n, destination_start_n, length).
    """
    seed_soil_map = re.search(rf"{map_name} map:[0-9  \n]+", fdata, re.DOTALL).group(0).strip()
    mapping = []
    for line in seed_soil_map.splitlines()[1:]:
        dest_start, src_start, size = map(int, line.split())
        mapping.append((src_start, dest_start, size))

    return mapping


maps = [
    create_mapping("seed-to-soil"),
    create_mapping("soil-to-fertilizer"),
    create_mapping("fertilizer-to-water"),
    create_mapping("water-to-light"),
    create_mapping("light-to-temperature"),
    create_mapping("temperature-to-humidity"),
    create_mapping("humidity-to-location")
]

seed_numbers = fdata[:fdata.index('\n')]
seed_numbers = seed_numbers.split(': ')[1]
seed_numbers = list(map(int, seed_numbers.split()))

location_numbers = []

for seed in seed_numbers:
    # Apply all maps where each "map" receives the output of previous map as input
    # by setting 'seed' to the mapped value.
    for mapping in maps:
        for entry in mapping:
            src_start, dest_start, size = entry
            if seed in range(src_start, src_start + size):
                # The input is only mapped by shifting, so if it is in range of the mapped values, just offset the input.
                # If it is not in range it means there is no mapping from the input to the output and we keep it the same.
                seed = seed + (dest_start - src_start)
                break

    location_numbers.append(seed)

print("Minimum location number:", min(location_numbers))
