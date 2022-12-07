value1 = 0
value2 = 0
f = open("day1y.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    if value1 > value2:
            value2 = value1
    else:
        value1 += int(line)
print(value2)