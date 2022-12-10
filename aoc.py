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

