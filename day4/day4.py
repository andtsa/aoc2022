if __name__ == "__main__":
    pass

f = open("day4.txt")
lines = f.readlines()

x = 0
y = 0

for line in lines:
    one = (line.split(","))[0].split("-")
    ass1 = [int(one[0]), int(one[1])]
    two = (line.split(","))[1].split("-")
    ass2 = [int(two[0]), int(two[1])]
    print(ass1)
    print(ass2)

    if ass1[0]<=ass2[0] and ass1[1]>=ass2[1]:
        x+=1
    elif ass1[1]<=ass2[1] and ass1[0]>=ass2[0]:
        x+=1

    if not (ass1[1] < ass2[0] or ass2[1] < ass1[0]):
        y+=1

print(x)
print(y)