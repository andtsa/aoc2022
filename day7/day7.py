if __name__ == "__main__":
    pass

f1 = open("day7.txt")
f2 = open("day7test.txt")
file = f1.read()
testf = f2.read()

lines = file.split("\n")

x = 0

tree = {
    ('/',): []
}

directories = []

currentDirectory = ()

l = -1
for line in lines:
    l += 1
    if line[0] == "$":
        if line[2] == "c":
            dir = line.split(" ")[2]
            if dir == "..":
                currentDirectory = currentDirectory[:len(currentDirectory)-1]
            else:
                currentDirectory += (dir,)
                if currentDirectory not in directories:
                    directories.append(currentDirectory)
        elif line[2] == "l":
            i = l
            while len(lines) > i+1 and lines[i + 1][0] != "$":
                i += 1
                currentLine = lines[i].split(" ")
                if currentLine[0] == "dir":
                    d = currentDirectory + (currentLine[1],)
                    tree[d] = []
                    if d not in directories:
                        directories.append(d)
                else:
                    tree[currentDirectory].append((int(currentLine[0]), currentLine[1]))

print(tree)
print(directories)

sizes = []

def getDirSize(f):
    t = tree[f]
    s = 0
    for i in t:
        s += i[0]
    return s

for folder in directories:
    sizesum = getDirSize(folder)
    #print(str(folder) + " has files : " + str(sizesum))
    for subfolder in directories:
        if subfolder[:len(folder)] == folder and subfolder!=folder:
            sizesum += getDirSize(subfolder)
    sizes.append(sizesum)

print(sizes)

# sizes.append(0)

disk = sizes[0]
valids = []
for s in sizes:
    if disk - s <= 40000000:
        valids.append(s)

print(min(valids))

# print(x)
