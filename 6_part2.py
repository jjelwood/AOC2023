input = open("6.txt").read()
test = """\
Time:      7  15   30
Distance:  9  40  200"""

from math import sqrt, ceil, floor
t = int("".join(input.split("\n")[0].split()[1:]))
r = int("".join(input.split("\n")[1].split()[1:]))

min = (t-sqrt(t**2-4*r))/2
max = (t+sqrt(t**2-4*r))/2
if min.is_integer():
    min += 1
if max.is_integer():
    max -= 1
min = ceil(min)
max = floor(max)
print(max-min+1)
