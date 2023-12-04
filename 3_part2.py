input = open("3.txt").read()
test = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..\
"""

import re

#input = test

y = len(input.split("\n"))
x = len(input.split("\n")[0])
input = input.replace("\n", "")
parts = re.finditer(r"\*", input)

gear_coords = []

for match in parts:
    i = match.start()
    number_locations = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (not 0 <= (i % x) + dx < x) or (not 0 <= (i // y) + dy < y):
                continue
            
            if re.match(r"\d", input[i + dx + y * dy]):
                number_locations.append(i + dx + y * dy)
    
    if i + y - 1 in number_locations and i + y in number_locations:
        if i + y + 1 in number_locations:
            number_locations.remove(i + y + 1)
        number_locations.remove(i + y)
    elif i + y in number_locations and i + y + 1 in number_locations:
        number_locations.remove(i + y + 1)
    
    if i - y - 1 in number_locations and i - y in number_locations:
        if i - y + 1 in number_locations:
            number_locations.remove(i - y + 1)
        number_locations.remove(i - y)
    elif i - y in number_locations and i - y + 1 in number_locations:
        number_locations.remove(i - y + 1)
    
    if len(number_locations) == 2:
        gear_coords.append(number_locations)

res = 0

for gear in gear_coords:
    numbers = []
    for i in gear:
        y_i = i // y
        x_i = i % x
        numbers_in_line = re.finditer("\d+", input[y_i * y : (y_i + 1) * y])
        for match in numbers_in_line:
            number = match.group()
            if match.start() <= x_i < match.end():
                numbers.append(int(number))
    res += numbers[0] * numbers[1]

print(res)