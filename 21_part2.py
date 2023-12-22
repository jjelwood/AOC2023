input = open("21.txt").read()

test = """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

test2 ="""\
...
.S.
...\
"""

test3 = """\
..###
.#S..
..###\
"""

import copy

input = test3
lines = input.split("\n")
Y = len(lines)
X = len(lines[0])
garden = input.replace("\n", "")

start = garden.find('S')
locations = {start}
location_zones = {x: set() for x in range(X*Y)}
location_zones[start].add("0,0")

def zone_hash(x, y):
    return f"{x},{y}"

def shift_zone(zone, dx, dy):
    x, y = [int(n) for n in zone.split(",")]
    return zone_hash(x + dx, y + dy)

n_steps = 5
for i in range(n_steps):
    if i % 10000 == 0:
        print(i)
    locations_move_from = list(locations)

    new_lzs = {x: set() for x in range(X*Y)}
    for location in locations_move_from:
        shift_left, shift_right, shift_up, shift_down = False, False, False, False
        locations.remove(location)

        if location % X != 0:
            left = location - 1 
        else:
            left = location + X - 1
            shift_left = True
        if location % X != X - 1:
            right = location + 1 
        else:
            right = location - X + 1
            shift_right = True
        if location // X != Y - 1:
            top = location + X 
        else:
            top = location % X
            shift_up = True
        if location // X != 0:
            bottom = location - X 
        else: 
            bottom = X * (Y - 1) + location
            shift_down = True

        if garden[left] != "#":
            locations.add(left)
            if shift_left:
                new_lzs[left] |= {shift_zone(zone, -1, 0) for zone in location_zones[location]}
            else:
                new_lzs[left] |= location_zones[location]
        if garden[right] != "#":
            locations.add(right)
            if shift_right:
                new_lzs[right] |= {shift_zone(zone, 1, 0) for zone in location_zones[location]}
            else:
                new_lzs[right] |= location_zones[location]
        if garden[top] != "#":
            locations.add(top)
            if shift_up:
                new_lzs[top] |= {shift_zone(zone, 0, 1) for zone in location_zones[location]}
            else:
                new_lzs[top] |= location_zones[location]
        if garden[bottom] != "#":
            locations.add(bottom)
            if shift_down:
                new_lzs[bottom] |= {shift_zone(zone, 0, -1) for zone in location_zones[location]}
            else:
                new_lzs[bottom] |= location_zones[location]
    
    print(i+1)
    for i in range(Y):
        for j in range(X):
            if X * i + j in locations:
                print("O", end="")
            else:
                print(garden[X * i  + j], end="")
        print()
    print()

    location_zones = new_lzs

result = 0

for location, zones in location_zones.items():
    print(location % X, location // X, zones)
    result += len(zones)

print(result)