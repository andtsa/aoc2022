if __name__ == "__main__":
    pass

f = open("day3.txt", "r")
filein = f.read()
lines = filein.split("\n")

x = 0

elfn = 0
for linenumber in range(len(lines)//3):
    print(linenumber)
    valids = []
    used = []
    for second in lines[3*linenumber+1]:
        if second in lines[3*linenumber]:
            valids.append(second)
    for third in lines[3*linenumber+2]:
        if third in valids and third not in used:
            used.append(third)
            if third.islower():
                x += ord(third) - 96
            else:
                x += ord(third) - 64 + 26



print(x)