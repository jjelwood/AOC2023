input = open("24.txt").read()
test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

min_l = 200000000000000
max_l = 400000000000000

class Hailstone:
    def __init__(self, pos, vel):
        self.x0 = pos[0]
        self.y0 = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.grad = vel[1] / vel[0]
    
    def calc_y(self, x):
        return self.grad * (x - self.x0) + self.y0
    
    def point_is_in_future(self, px, py):
        if self.vx > 0 and px < self.x0:
            return False
        if self.vx < 0 and px > self.x0:
            return False 
        if self.vy > 0 and py < self.y0:
            return False
        if self.vy < 0 and py > self.y0:
            return False 
        return True

    def calc_intercept(self, other):
        if self.grad == other.grad:
            if self.calc_y(other.x0) == other.y0:
                return True
            else:
                return False
        x_intercept = (self.grad * self.x0 - other.grad * other.x0 - self.y0 + other.y0) / (self.grad - other.grad)
        intercepts = (x_intercept, self.calc_y(x_intercept))
        if not self.point_is_in_future(*intercepts) or not other.point_is_in_future(*intercepts):
            return False
        return intercepts
        

hailstones = [Hailstone(info[0], info[1]) for info in [[tuple(int(x) for x in group.split(",")) for group in line.split("@")] for line in input.replace(" ", "").split("\n")]]

count = 0
for i, h1 in enumerate(hailstones[:-1]):
    for h2 in hailstones[i+1:]:
        intercept = h1.calc_intercept(h2)
        # print(intercept)
        if type(intercept) is bool:
            if intercept == True:
                count += 1
            continue
        if min_l <= intercept[0] <= max_l and min_l <= intercept[1] <= max_l:
            count += 1
print(count)



