input = open("6.txt").read()
test = """\
Time:      7  15   30
Distance:  9  40  200"""

from math import sqrt, ceil, floor
t = int("".join(input.split("\n")[0].split()[1:]))
r = int("".join(input.split("\n")[1].split()[1:]))

min = floor((t-sqrt(t**2-4*r))/2+1)
max = ceil((t+sqrt(t**2-4*r))/2-1)
print(max-min+1)
