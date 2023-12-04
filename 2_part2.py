input = open("2.txt").read()

input = [line.split(":") for line in input.split("\n")]

res = 0

for line in input:
    max_counts = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for set in line[1].split("; "):
        counts = {}
        for draw in set.split(", "):
            draw = draw.split()
            counts[draw[1]] = counts.get(draw[1], 0) + int(draw[0])
            max_counts[draw[1]] = max(counts[draw[1]], max_counts[draw[1]])
       
        for color in counts.keys():
                counts[color] = 0
    
    print(max_counts)
    
    #print(int(line[0].split()[1]))
    res += max_counts["red"] * max_counts["blue"] * max_counts["green"]

print(res)
