import math
import time
from aoc import *
from collections import defaultdict, deque
if __name__ == "__main__" or 1:
    mode = 0
    day = 18

lines, t0 = init(day, mode)
# f = open('day18.txt').read().strip()
# lines = f.split("\n")

# # #
size = -1
for line in lines:
    x, y, z = line.split(',')
    size = max(size, int(x), int(y), int(z))

size += 1
print("grid with size:", size)

grid = [[[0 for _ in range(-1, size)] for _ in range(-1, size)] for _ in range(-1, size)]
points = set()

for line in lines:
    x, y, z = line.split(',')
    grid[int(x)][int(y)][int(z)] = 1
    points.add((int(x),int(y), int(z)))


checkedX = set()
checkedY = set()
checkedZ = set()


def scansquareX(x, y, z):
    if (x, y, z) in checkedX:
        return 0
    checkedX.add((x, y, z))
    s = 0
    if grid[x][y][z] == 0:
        return s
    # check x-1
    if x <= 0:
        s += 1
    elif grid[x - 1][y][z] == 0:
        s += 1
    else:
        s += scansquareX(x - 1, y, z)
    # check x+1
    if x >= len(grid):
        s += 1
    elif grid[x + 1][y][z] == 0:
        s += 1
    else:
        s += scansquareX(x + 1, y, z)
    return s


def scansquareY(x, y, z):
    if (x, y, z) in checkedY:
        return 0
    checkedY.add((x, y, z))
    s = 0
    if grid[x][y][z] == 0:
        return s
    # check y-1
    if y <= 0:
        s += 1
    elif grid[x][y - 1][z] == 0:
        s += 1
    else:
        s += scansquareY(x, y - 1, z)
    # check y+1
    if y >= len(grid[x]):
        s += 1
    elif grid[x][y + 1][z] == 0:
        s += 1
    else:
        s += scansquareY(x, y + 1, z)
    return s


def scansquareZ(x, y, z):
    if (x, y, z) in checkedZ:
        return 0
    checkedZ.add((x, y, z))
    s = 0
    if grid[x][y][z] == 0:
        return s
    # check z-1
    if z <= 0:
        s += 1
    elif grid[x][y][z - 1] == 0:
        s += 1
    else:
        s += scansquareZ(x, y, z - 1)
    # check y+1
    if z >= len(grid[x][y]):
        s += 1
    elif grid[x][y][z + 1] == 0:
        s += 1
    else:
        s += scansquareZ(x, y, z + 1)
    return s


sides = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        for z in range(len(grid[x][y])):
            if (x, y, z) not in checkedX:
                sides += scansquareX(x, y, z)
            if (x, y, z) not in checkedY:
                sides += scansquareY(x, y, z)
            if (x, y, z) not in checkedZ:
                sides += scansquareZ(x, y, z)

print("part one:", sides)

dt(t0)

# part two
outer = set()
inner = set()
def enclosed(x, y, z):
    if (x, y, z) in inner:
        return 1
    if (x, y, z) in outer:
        return 0
    checked = set()
    dq = deque()
    dq.append((x, y, z))
    while dq:
        x,y,z = dq.popleft()
        if (x,y,z) in points:
            continue
        if (x,y,z) in checked:
            continue
        checked.add((x,y,z))
        if len(checked) > 5000:
            for p in checked:
                outer.add(p)
            return 0
        dq.append((x+1,y,z))
        dq.append((x-1,y,z))
        dq.append((x,y+1,z))
        dq.append((x,y-1,z))
        dq.append((x,y,z+1))
        dq.append((x,y,z-1))
    for p in checked:
        inner.add(p)
    return 1


s = 0
for x, y, z in points:
    if not enclosed(x - 1, y, z):
        s += 1
    if not enclosed(x + 1, y, z):
        s += 1
    if not enclosed(x, y - 1, z):
        s += 1
    if not enclosed(x, y + 1, z):
        s += 1
    if not enclosed(x, y, z - 1):
        s += 1
    if not enclosed(x, y, z + 1):
        s += 1
print("part two: ", s)
dt(t0)
