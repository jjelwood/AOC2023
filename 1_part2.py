import re
import math
lines = open("1.txt").read()
test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
#lines = test
lines = lines.split("\n")

new_lines_forward = []
new_lines_backwards = []
for line in lines:
    indices_f = []
    indices_b = []
    for key, value in digits.items():
        match_f = re.search(key, line)
        match_b = re.search(key[::-1], line[::-1])
        indices_f.append((match_f.start() if match_f is not None else math.inf, key))
        indices_b.append((match_b.start() if match_b is not None else math.inf, key))

    indices_f.sort(key=lambda x: x[0])
    indices_b.sort(key=lambda x: x[0])

    new_line_forward = line
    new_line_backwards = line

    for index in indices_f:
        new_line_forward = new_line_forward.replace(index[1], digits[index[1]])
    for index in indices_b:
        new_line_backwards = new_line_backwards.replace(index[1], digits[index[1]])
    
    new_lines_forward.append(new_line_forward)
    new_lines_backwards.append(new_line_backwards)

lines_forwards = [[int(c) for c in line if c.isdigit()] for line in new_lines_forward]
lines_backwards = [[int(c) for c in line if c.isdigit()] for line in new_lines_backwards]

lines = [lines_forwards[i][0] * 10 + lines_backwards[i][-1] for i in range(len(lines))]
print(sum(lines))