input = open("4.txt").read()
test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

#input = test

lines = [[set(numbers.split()) for numbers in line.split(":")[1].split(" | ")] for line in input.split("\n")]
winning_numbers = [len(line[0].intersection(line[1])) for line in lines]
copies = [1 for _ in winning_numbers]

for i, n in enumerate(winning_numbers):
    for j in range(i+1, i+1+n):
        copies[j] += copies[i]

print(sum(copies))
