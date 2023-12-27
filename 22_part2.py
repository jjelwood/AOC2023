input = open("22.txt").read()

test = """\
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9\
"""

test2 = """\
0,1,4~2,1,4
1,0,6~1,2,6\
"""

test3 = """\
2,0,1~4,0,1
1,0,2~2,0,2
4,0,2~5,0,2
2,0,3~4,0,3\
"""

class Brick:
    def __init__(self, start, end):
        self.vel = [0, 0, 0]
        for i in range(3):
            if start[i] - end[i] != 0:
                if start[i] > end[i]:
                    start, end = end, start
                self.vel[i] = 1
                self.len = end[i] - start[i] + 1
                break
        else:
            self.len = 1
        self.start = start
        self.end = end
        self.bricks_above = set()
        self.bricks_below = set()

    def get_squares(self):
        res = set()
        for i in range(self.len):
            res.add((self.start[0] + i * self.vel[0], self.start[1] + i * self.vel[1], self.start[2] + i * self.vel[2]))
        return res        
    
    def get_blocked_squares(self):
        res = set()
        for i in range(self.len):
            res.add((self.start[0] + i * self.vel[0], self.start[1] + i * self.vel[1], self.start[2] + i * self.vel[2] + 1))
        return res
    
    def fall(self):
        self.start[2] -= 1
        self.end[2] -= 1

bricks = [Brick(*[list(map(int, brick.split(","))) for brick in line.split("~")]) for line in input.split("\n")]
blocked_squares = set()
blocked_squares_to_bricks = {}

# Lowest bricks fall first
fall_stack = sorted(bricks, key=lambda brick: brick.start[2], reverse=True)

while fall_stack:
    brick = fall_stack.pop()

    while brick.start[2] > 1:
        support_squares = blocked_squares & brick.get_squares()
        if len(support_squares) > 0:
            for square in support_squares:
                brick.bricks_below.add(blocked_squares_to_bricks[square])
                blocked_squares_to_bricks[square].bricks_above.add(brick)
            break
        
        brick.fall()
    
    for square in brick.get_blocked_squares():
        blocked_squares.add(square)
        blocked_squares_to_bricks[square] = brick

count = 0
for brick in bricks:
    bricks_to_fall = [brick]
    fallen_bricks = set()
    while bricks_to_fall:
        next_brick = bricks_to_fall.pop(0)
        fallen_bricks.add(next_brick)

        for brick_above in next_brick.bricks_above:
            if len(brick_above.bricks_below - fallen_bricks) == 0:
                bricks_to_fall.append(brick_above)
                count += 1

print(count)