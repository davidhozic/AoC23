import re


with open("input.txt") as file:
    fdata = file.read()


def create_mapping(map_name: str):
    """
    Creates a list of parsed tuples that contain (source_start_n, offset, length).
    """
    seed_soil_map = re.search(rf"{map_name} map:[0-9  \n]+", fdata, re.DOTALL).group(0).strip()
    mapping = []
    for line in seed_soil_map.splitlines()[1:]:
        dest_start, src_start, size = map(int, line.split())
        mapping.append((src_start, dest_start - src_start, size))

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


# Practically the same as part1, we only need to create extra seeds from ranges
seed_number_ranges = fdata[:fdata.index('\n')]
seed_number_ranges = seed_number_ranges.split(': ')[1]
seed_number_ranges = list(map(int, seed_number_ranges.split()))
# Each 2 elements represent the start seed and the length
seed_number_ranges = [seed_number_ranges[i:i+2] for i in range(0, len(seed_number_ranges), 2)]



per_map_ranges = [(seed_start, seed_start + seed_length) for seed_start, seed_length in seed_number_ranges]
# Here we map out our input ranges that overlap with the map output.
# So we basically throw away any of the input range that does not have a mapping and then
# we process each of the sub-ranges.
for mapping in maps:
    new_ranges = []
    for sstart, send in per_map_ranges:
        for in_start, offset, in_length in mapping:
            in_end = in_start + in_length
            in_start = max(in_start, sstart)  # Create a sub-range that overlaps with current mapping line
            in_end = min(in_end, send)
            if in_start < in_end:  # If it overlaps
                new_ranges.append((in_start + offset, in_end + offset))

    per_map_ranges = new_ranges  # The output of current map is the input to the next map

print("Minimal one:", min(per_map_ranges, key=lambda x: x[0])[0])  # Now find the minimal start of the range
