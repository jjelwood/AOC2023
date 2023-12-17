input = open("6.txt").read()
test = """\
Time:      7  15   30
Distance:  9  40  200"""

from math import sqrt, ceil, floor
times = [int(t) for t in input.split("\n")[0].split()[1:]]
records = [int(t) for t in input.split("\n")[1].split()[1:]]
n_ways = []
print(times, records)
for i in range(len(times)):
    t = times[i]
    r = records[i]
    print(t, r)
    min = (t-sqrt(t**2-4*r))/2
    max = (t+sqrt(t**2-4*r))/2
    if min.is_integer():
        min += 1
    if max.is_integer():
        max -= 1
    min = ceil(min)
    max = floor(max)
    n_ways.append(max-min+1)

print(n_ways)
result = 1
for n in n_ways:
    result *= n

print(result)
