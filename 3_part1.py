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

y = len(input.split("\n"))
x = len(input.split("\n")[0])
input = input.replace("\n", "")
parts = re.finditer(r"[^\d\.]", input)

number_coords = []

for match in parts:
    i = match.start()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (not 0 <= (i % x) + dx < x) or (not 0 <= (i // y) + dy < y):
                continue
            
            if re.match(r"\d", input[i + dx + y * dy]):
                number_coords.append(i + dx + y * dy)

matches = []
visited = set()
for i in number_coords:
    y_i = i // y
    x_i = i % x
    numbers_in_line = re.finditer("\d+", input[y_i * y : (y_i + 1) * y])
    for match in numbers_in_line:
        number = match.group()
        if match.start() <= x_i < match.end() and match.start() + y * y_i not in visited:
            matches.append(number)
            visited.add(match.start() + y * y_i)

numbers = [int(match) for match in matches]
print(sum(numbers))
