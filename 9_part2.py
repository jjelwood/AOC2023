input = open("9.txt").read()
test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

sequences = input.split("\n")
nexts = []

"""
import numpy as np
import numpy.polynomial.polynomial as pol
for sequence in sequences:
    ys = np.array([int(n) for n in sequence.split()])
    xs = np.arange(0, ys.size)
    coeffs = pol.polyfit(xs, ys, xs.size - 1)
    nexts.append(pol.polyval(xs.size, coeffs))"""

def calc_differences(ns):
    return [ns[i + 1] - ns[i] for i in range(len(ns)-1)]

for sequence in sequences:
    ns = [int(n) for n in sequence.split()]
    differences = calc_differences(ns)
    differences_of_first_terms = [differences[0]]
    while any(differences):
        differences = calc_differences(differences)
        differences_of_first_terms.append(differences[0])
    nexts.append(sum(-n if i % 2 == 0 else n for i, n in enumerate(differences_of_first_terms)) + ns[0])

print(nexts)
print(sum(nexts))