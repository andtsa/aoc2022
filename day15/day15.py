import math
import time
from aoc import *
if __name__ == "__main__" or 1:
    mode = 0
    day = 15

lines, t0 = init(day, mode)
sensors = set()
beacons = set()
for line in lines:
    line = line.split(" ")
    sx = int(line[2][2:-1])
    sy = int(line[3][2:-1])
    bx = int(line[8][2:-1])
    by = int(line[9][2:])
    d = tdist([sx, sy], [bx, by])
    beacons.add((bx, by))
    sensors.add((sx, sy, d))


def validPos(x, y):
    if (x, y) in beacons:
        return False
    for s in sensors:
        if tdist(s, [x, y]) <= s[2]:
            return False
    return True


# look through row for pt1
part_one = set()
y = 10 if mode else 2000000
n = int(5e6)
t = time.time_ns()
for x in range(-n, n):
    if x % (n/(precision:=10)) == 0:
        if n-abs(x) > 0:
            print(str(pc := (50 * (x + n) / n)) + "%", end="  ")
            print("estimating: "+str(est:=math.ceil(((time.time_ns()-t)*(10**-7))/pc))+" seconds. only " +
                  str(math.ceil((100-pc)*est*0.01))+"s left")
    if not(validPos(x, y)) and (x, y) not in beacons:
        part_one.add((x, y))

print("Part one:", len(part_one))


# for part 2, we need to search the perimeter of each sensor's view
# if there is a spot that no sensor sees and is on some sensor's perimeter
# then only that can be the distress beacon

min_xy = 0
max_xy = 20 if mode else 4000000
sensors_done = 0
found = 0
for (sx, sy, d) in sensors:
    # we scan the area of each sensor + 1 line outside each side (d-1,d+1), hence d+2
    for w in range(d+2):
        if found:break
        h = d - w + 1
        for side in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x = sx + (w * side[0])
            y = sy + (h * side[1])
            if not (min_xy <= x <= max_xy and min_xy <= y <= max_xy) or not (abs(x - sx) + abs(y - sy) == d + 1):
                continue
            if validPos(x, y):
                print("Part two:", x * 4000000 + y)
                print("at:", (x, y))
                found = 1
    if found:break
    print(sensors_done:=sensors_done+1,"sensor(s) done of",len(sensors))

dt(t0)
