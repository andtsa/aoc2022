if __name__ == "__main__":
    pass

f = open("day5.txt")
f2 = open("day5test.txt")
filein = f.read()
testin = f2.read()

parts = filein.split("\n\n")       #####

# print(parts)

x = 0
height = -1
stacks = []

for _ in range(9):             #####
    stacks.append([])

section1 = parts[0].split("\n")
section1.pop()

# print(section1)

for line in section1:
    if line.strip() == "":
        continue
    #stack = (len(line) - len(line.lstrip()))//4

    for n in range(9):               #####
        if 4*n+1 > len(line):
            break
        elif not line[4*n +1] == " ":
            stacks[n].append(line[4*n +1])

# print(stacks)

for j in range(len(stacks)):
    stacks[j].reverse()

print(stacks)

for i in parts[1].split("\n"):
    l = i.split(" ")
    first = int(l[1])
    second = int(l[3])-1
    third = int(l[5])-1

    movingarray = []

    for times in range(first):
        if len(stacks[second]) == 0:
            continue
        movingarray.append(stacks[second].pop())
    movingarray.reverse()
    for m in movingarray:
        stacks[third].append(m)

print(stacks)

res = ""

for q in stacks:
    res += q.pop()

print(res)





# for chars in parts[1].split("\n"):
#     l = chars.split(" ")
#     first = int(l[1])
#     second = int(l[3])-1
#     third = int(l[5])-1
#
#     for times in range(first):
#         if len(stacks[second]) == 0:
#             continue
#         stacks[third].append(stacks[second].pop())
#         print(stacks)