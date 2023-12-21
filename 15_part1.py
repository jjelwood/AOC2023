input = open("15.txt").read()

def hash(string):
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256
    return result

print(sum(hash(s) for s in input.split(",")))