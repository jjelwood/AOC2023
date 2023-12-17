test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class IntervalMap:
    def __init__(self):
        self.intervals = []
    
    def add_interval(self, dest_start, source_start, length):
        self.intervals.append((dest_start, source_start, length))
    
    def calc_map(self, source_n):
        for interval in self.intervals:
            if 0 <= source_n - interval[1] < interval[2]:
                return interval[0] + source_n - interval[1]
        return source_n

input = open("5.txt").read()
input = test
input = input.split("\n\n")

seed_numbers = [int(n) for n in input.pop(0).split()[1:]]

seed_intervals = []

i = 0
while i < len(seed_numbers):
    start = seed_numbers[i]
    length = seed_numbers[i+1]
    seed_intervals.append([start, start + length])
    i += 2

seed_intervals.sort(key=lambda i: i[1])

maps = []

for map_lines in input:
    intervalmap = IntervalMap()
    for line in map_lines.split("\n")[1:]:
        intervalmap.add_interval(*[int(n) for n in line.split()])
    maps.append(intervalmap)

print(seed_intervals)

for intervalmap in maps:
    new_seeds = []
    for map_interval in intervalmap.intervals:
        # map_source[0] is the start of the mapping's source interval
        # map_source[1] is the end of the mapping's source interval
        map_source = [map_interval[1], map_interval[1] + map_interval[2]]
        for seed_interval in seed_intervals:
            # If source intervals don't intersect at all i.e.
            # seed: __
            # map:     ___
            # or
            # seed:     __
            # map:  ___
            if map_source[1] < seed_interval[0] or \
                map_source[0] >= seed_interval[1]:
                pass

            # Partial intersection seed > map i.e.
            # seed:   ____
            # map:  ____
            elif seed_interval[0] <= map_interval[1] < seed_interval[1] and \
                map_source[0] < map_source[0]:
                new_seeds.append([map_interval[0], map_interval[0] + map_source[1] - seed_interval[0]])
                seed_interval[0], seed_interval[1] = map_interval[1], seed_interval[1]

            # Partial intersection map > seed i.e.
            # seed: ____
            # map:    ____
            elif seed_interval[0] <= map_interval[0] < seed_interval[1] and \
                map_interval[1] > seed_interval[1]:
                new_seeds.append([map_interval[0], map_interval[0] + seed_interval[1] - map_source[0]])
                seed_interval[0], seed_interval[1] = seed_interval[1], map_interval[1]
            
            # Full overlap |seed| > |map| i.e.
            # seed:  ______
            # map:    ___
            elif seed_interval[0] <= map_interval[0] and seed_interval[1] > map_interval[1]:
                new_seeds.append([map_interval[0], map_interval[0] + map_interval[2]])
                seed_intervals.append([seed_interval[0], map_interval[0]])
                seed_interval[1] = map_interval[0]

            # Full overlap |seed| < |map| i.e.
            # seed:  ____
            # map:  ______
            else:
                new_seeds.append([map_interval[0] + seed_interval[0] - map_source[0], map_interval[0] + map_source[1] - seed_interval[1]])
        for seed_interval in seed_intervals:
            new_seeds.append(seed_interval)
    seed_intervals = new_seeds
    
new_seeds.sort(key=lambda x: x[0])

print(min(new_seeds[0]))
