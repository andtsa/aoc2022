import time


def printGrid(grid):
    for g in grid:
        for d in g:
            print(d, end=" ")
        print(end="\n")
    print(end="\n")

def hasDuplicates(x):
    k = 0
    for l in range(len(x)-1):
        k=l+1
        for l in range(k):
            if x[l]==x[k]:
                return True
    return False


def tdist(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])


def init(day, mode):
    infile = "day" + str(day) + mode * "test" + ".txt"
    text = open(infile).read().strip()
    lines = [x for x in text.split('\n')]
    t0 = time.time_ns()
    return lines, t0


def dt(t0):
    print("\ndt: " + str((time.time_ns()-t0)/10**6) + "ms")
