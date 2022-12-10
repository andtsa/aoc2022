if __name__ == "__main__":
    pass

fileinput = open("day9.txt").read()
testinput = open("day9test.txt").read()

lines = testinput.split("\n")

head = [0, 0]
tail = [0, 0]

x = 0
longtail = [[0, 0] for _ in range(9)]
visited = []


def printGrid(h, t):
    hx = (h[0] + abs(h[0])) // 2
    hy = (h[1] + abs(h[1])) // 2
    tx = (t[0] + abs(t[0])) // 2
    ty = (t[1] + abs(t[1])) // 2
    height = 1 + max([hx, hy, tx, ty])
    grid = [["." for _ in range(height)] for _ in range(height)]
    grid[tx][ty] = "T"
    grid[hx][hy] = "H"
    for g in grid:
        for d in g:
            print(d, end=" ")
        print(end="\n")
    print(end="\n")


def tailFollow(h, t):
    δv = abs(h[0] - t[0])
    δh = abs(h[1] - t[1])
    printGrid(h, t)
    if δv > 2 and δh > 2:
        t = [h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1]
    elif δv > 1:
        t[1] = h[1]
        if t[0] < h[0]:
            t[0] = h[0] - 1
        else:
            t[0] = h[0] + 1
    elif δh > 1:
        t[0] = h[0]
        if t[1] < h[1]:
            t[1] = h[1] - 1
        else:
            t[1] = h[1] + 1
    return t


for line in lines:
    move = line[0]
    steps = int(line.split(" ")[1])

    # moving up
    if move == "U":
        for m in range(steps):
            head[0] += 1
            #printGrid(head, tail)
            longtail[0] = tailFollow(head, longtail[0])
            for segment in range(1, len(longtail)):
                longtail[segment] = tailFollow(longtail[segment - 1], longtail[segment])
            if head[0] > tail[0]+1:
                x += 1
                tail[0] += 1
                if head[1] != tail[1]:
                    tail[1] = head[1]
            #printGrid(head, tail)

    # moving down
    if move == "D":
        for m in range(steps):
            head[0] += -1
            #printGrid(head, tail)
            longtail[0] = tailFollow(head, longtail[0])
            for segment in range(1, len(longtail)):
                longtail[segment] = tailFollow(longtail[segment - 1], longtail[segment])
            if head[0] < tail[0] - 1:
                x += 1
                tail[0] += -1
                if head[0] != tail[0]:
                    tail[0] = head[0]
            #printGrid(head, tail)

    # moving left
    if move == "L":
        for m in range(steps):
            head[1] += -1
            #printGrid(head, tail)
            longtail[0] = tailFollow(head, longtail[0])
            for segment in range(1, len(longtail)):
                longtail[segment] = tailFollow(longtail[segment - 1], longtail[segment])
            if head[1] < tail[1] - 1:
                x += 1
                tail[1] += -1
                if head[0] != tail[0]:
                    tail[0] = head[0]
            #printGrid(head, tail)

    # moving up
    if move == "R":
        for m in range(steps):
            head[1] += 1
            #printGrid(head, tail)
            longtail[0] = tailFollow(head, longtail[0])
            for segment in range(1, len(longtail)):
                longtail[segment] = tailFollow(longtail[segment - 1], longtail[segment])
            if head[1] > tail[1] + 1:
                x += 1
                tail[1] += 1
                if head[0] != tail[0]:
                    tail[0] = head[0]
            #printGrid(head, tail)
    if longtail[-1] not in visited:
        visited.append(longtail[-1])


print("Part one: ", x)
print("Part two: ", len(visited))
