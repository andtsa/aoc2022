from aoc import *

if __name__ == "__main__":
    pass

fileinput = open("day10.txt").read()
testinput = open("day10test.txt").read()

lines = fileinput.split("\n")

r = 1
cycle = 0
sum = 0
queue = []
screen = [["."for _ in range(40)]for _ in range(6)]


for line in lines:
    print(r)
    cycle += 1
    x = (cycle-1) % 40
    y = cycle//40

    if line == "noop":
        queue.append(0)

    if line.split(" ")[0] == "addx":
        a = int(line.split(" ")[1])
        queue.append(0)
        queue.append(a)

    if (cycle-20) % 40 == 0:
        sum += cycle * r

    if (cycle-1) % 40 in [r-1, r, r+1]:
        screen[y][x] = "#"

    r += queue.pop(0)

for instruction in queue:
    cycle += 1
    x = (cycle - 1) % 40
    y = cycle // 40
    if (cycle-20) % 40 == 0:
        sum += cycle * r
    if (cycle-1) % 40 in [r-1, r, r+1]:
        screen[y][x] = "#"
    r += instruction


print(sum)
printGrid(screen)

