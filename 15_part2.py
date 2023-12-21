input = open("15.txt").read()

def hash(string):
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256
    return result

boxes = {i: [] for i in range(256)}
commands = input.split(",")
for command in commands:
    if command.endswith("-"):
        label = command[:-1]
        box = hash(label)
        for lens in boxes[box]:
            if lens[0] == label:
                boxes[box].remove(lens)
                break
    elif command[-2] == "=": 
        label = command[:-2]
        box = hash(label)
        n = int(command[-1])
        for lens in boxes[box]:
            if lens[0] == label:
                lens[1] = n
                break
        else:
            boxes[box].append([label, n])

result = 0
for i, box in boxes.items():
    for j, lens in enumerate(box):
        result += (i + 1) * (j + 1) * lens[1]

print(result)
        