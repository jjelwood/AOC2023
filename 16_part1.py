input = open("16.txt").read()
test = """\
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....\
"""

#input = test
lines = input.split("\n")
layout = input.replace("\n", "")
Y = len(lines)
X = len(lines[0])

if layout[0] in "-.":
    beams = [[0, 1]]
elif layout[0] in "\\|":
    beams = [[0, X]]
else:
    beams = [[0, -X]]

locations_and_vels = set()
energized_locations = set()

def hash(location, vel):
    return f"{location} {vel}"

while beams:
    location, vel = beams.pop(0)

    while hash(location, vel) not in locations_and_vels:
        locations_and_vels.add(hash(location, vel))
        energized_locations.add(location)
        if location % X == 0 and vel == -1:
            break
        if location % X == X - 1 and vel == 1:
            break
        if location // X == 0 and vel == -X:
            break
        if location // X == Y - 1 and vel == X:
            break

        location += vel
        # print(location)
        if layout[location] == "|" and abs(vel) == 1:
            beams.append([location, -X])
            vel = X
        elif layout[location] == "-" and abs(vel) == X:
            beams.append([location, -1])
            vel = 1
        elif layout[location] == "/":
            if vel == 1:
                vel = -X
            elif vel == -X:
                vel = 1
            elif vel == -1:
                vel = X
            else:
                vel = -1
        elif layout[location] == "\\":
            if vel == 1:
                vel = X
            elif vel == X:
                vel = 1
            elif vel == -1:
                vel = -X
            else:
                vel = -1

print(len(energized_locations))