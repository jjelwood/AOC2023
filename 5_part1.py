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

class RangeMap:
    def __init__(self):
        self.intervals = []
    
    def add_interval(self, dest_start, source_start, length):
        self.intervals.append((dest_start, source_start, length))
    
    def calc_map(self, source_n):
        for interval in self.intervals:
            if interval[1] <= source_n < interval[1] + interval[2]:
                return interval[0] + source_n - interval[1]
        return source_n

input = open("5.txt").read()
#input = test
input = input.split("\n\n")

seeds = [int(n) for n in input.pop(0).split()[1:]]

maps = []

for map_lines in input:
    rangemap = RangeMap()
    for line in map_lines.split("\n")[1:]:
        rangemap.add_interval(*[int(n) for n in line.split()])
    maps.append(rangemap)

locations = []
for seed in seeds:
    n = seed
    for rangemap in maps:
        n = rangemap.calc_map(n)
    locations.append(n)

print(maps[0].intervals)

print(min(locations))
