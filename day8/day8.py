if __name__ == "__main__":
    pass

fileinput = open("day8.txt").read()
testinput = open("day8test.txt").read()

lines = testinput.split("\n")

x = 0
y = []

grid = [[int(z) for z in line] for line in lines]

for row in range(1,len(grid)-1):
    for col in range(1,len(grid[row])-1):
        height = grid[row][col]
        # check above
        for above in range(row):
            if height <= grid[above][col]:
                break
        else:
            x+=1
            print("valid for "+ str(row)+","+str(col))
            continue
        # check below
        for below in range(row+1, len(grid)):
            if height <= grid[below][col]:
                break
        else:
            x+=1
            print("valid for "+ str(row)+","+str(col))

            continue
        # check left
        for left in range(col):
            if height <= grid[row][left]:
                break
        else:
            x += 1
            print("valid for "+ str(row)+","+str(col))

            continue
        # check right
        for right in range(col+1, len(grid[row])):
            if height <= grid[row][right]:
                break
        else:
            x += 1
            print("valid for "+ str(row)+","+str(col))
            continue

x += len(grid) * 2      # add sides
x += len(grid[0]) * 2   # add top & bottom
x -= 4                  # remove doubled corners

print("Part one: ", x)



# part two
x = 0
views = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        height = grid[row][col]
        x = 0
        view_score = 1
        # check above
        for above in range(row):
            x += 1
            if height <= grid[above][col]:
                break
        view_score *= x
        x=0
        # check below
        for below in range(row+1, len(grid)):
            x += 1
            if height <= grid[below][col]:
                break
        view_score *= x
        x = 0
        # check left
        for left in range(col):
            x += 1
            if height <= grid[row][left]:
                break
        view_score *= x
        x = 0
        # check right
        for right in range(col+1, len(grid[row])):
            x += 1
            if height <= grid[row][right]:
                break
        view_score *= x
        views.append(view_score)

print("Part two: ", max(views))
