input = open("12.txt").read()
test = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1\
"""

def input_to_hash(config, counts):
    return config + ",".join(str(n) for n in counts)

def count_arrangements(config, counts, cache):
    hash = input_to_hash(config, counts)
    if hash in cache:
        return cache[hash]

    if not config:
        return 0 if counts else 1
    
    if not counts:
        return 0 if "#" in config else 1
    
    result = 0

    # treat the first element as a .
    if config[0] == "." or config[0] == '?':
        result += count_arrangements(config[1:], counts, cache)
    
    # treat the first element as a #
    if config[0] == "#" or config[0] == "?":
        if "." not in config[:counts[0]] and len(config) >= counts[0]:
            new_counts = counts[1:] if len(counts) != 1 else []
            if len(config) != counts[0]:
                if config[counts[0]] != "#":
                    new_combination = config[counts[0]+1:]
                    result += count_arrangements(new_combination, new_counts, cache)
            else:
                new_combination = config[counts[0]:]
                result += count_arrangements(new_combination, new_counts, cache)

    cache[hash] = result

    return result

lines = [["?".join(springs for _ in range(5)), [int(n) for n in groups.split(",")]*5] for springs, groups in [line.split() for line in input.split("\n")]]

result = 0
for i, line in enumerate(lines):
    result += count_arrangements(line[0], line[1], cache={})

print(result)
