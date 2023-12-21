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

input = test
lines = input.split("\n")
Y = len(lines)
X = len(lines[0])
garden = input.replace("\n", "")

locations = {f"{garden.find('S')},0,0"}
n_steps = 50
for i in range(n_steps):
    print(i)
    locations_move_from = list(locations)
    for j in range(len(locations_move_from)):
        location, x, y = [int(n) for n in locations_move_from.pop(0).split(",")]
        locations.remove(location)
        if location % X != 0:
            left = location - 1 
            left_hash = f"{left},{x},{y}" 
        else:
            left = location + X - 1
            left_hash = f"{left},{x-1},{y}"
        if location % X != X - 1:
            right = location + 1 
        else:
            right = location - X + 1
            right_hash = f"{right},{x+1},{y}"
        if location // X != Y - 1:
            top = location + X 
            top_hash = f"{top},{x},{y+1}"
        else:
            top = location % X
        if location // X != 0:
            bottom = location - X 
            bottom_hash = f"{bottom},{x},{y}"
        else: 
            bottom = Y * (X - 1) + location % X
            bottom_hash = f"{bottom},{x},{y-1}"
        if garden[left] != "#":
            if left_hash not in locations:
                locations.add(left_hash)
        if garden[right] != "#":
            if right_hash not in locations:
                locations.add(right_hash)
        if garden[top] != "#":
            if top_hash not in locations:
                locations.add(top_hash)
        if garden[bottom] != "#":
            if bottom_hash not in locations:
                locations.add(bottom_hash)

print(len(locations))