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

def count_energized_tiles(start, start_vel):
    if layout[start] == "|" and abs(start_vel) == 1:
        beams = [[start, -X], [start, X]]
    elif layout[start] == "-" and abs(start_vel) == X:
        beams = [[start, -1], [start, 1]]
    elif layout[start] == "/":
        if start_vel == 1:
            vel = -X
        elif start_vel == -X:
            vel = 1
        elif start_vel == -1:
            vel = X
        else:
            vel = -1
        beams = [[start, vel]]
    elif layout[start] == "\\":
        if start_vel == 1:
            vel = X
        elif start_vel == X:
            vel = 1
        elif start_vel == -1:
            vel = -X
        else:
            vel = -1
        beams = [[start, vel]]
    else:
        beams = [[start, start_vel]]
    

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

    return len(energized_locations)

starts = []

for row in range(Y):
    starts.append([row * X, 1])
    starts.append([(row + 1) * X - 1, -1])    

for col in range(X):
    starts.append([col, X])
    starts.append([X * (Y - 1) + col, -X])

print(max(count_energized_tiles(*start) for start in starts))