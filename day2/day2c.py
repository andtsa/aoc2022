input = open("day2.txt", "r")

data = input.read()

data_list = []
total = 0

data_list = data.split("\n")

for i in range(len(data_list)):

    if data_list[i] == 'A X':
        total += (1 + 3)
    elif data_list[i] == 'A Y':
        total += (2 + 6)
    elif data_list[i] == 'A Z':
        total += (3 + 0)
    elif data_list[i] == 'B X':
        total += (1 + 0)
    elif data_list[i] == 'B Y':
        total += (2 + 3)
    elif data_list[i] == 'B Z':
        total += (3 + 6)
    elif data_list[i] == 'C X':
        total += (1 + 6)
    elif data_list[i] == 'C Y':
        total += (2 + 0)
    elif data_list[i] == 'C Z':
        total += (3 + 3)
    else:
        break
print("Part One")
print(total)

total = 0
for i in range(len(data_list)):

    if data_list[i] == 'A X':
        total += (3 + 0)
    elif data_list[i] == 'A Y':
        total += (1 + 3)
    elif data_list[i] == 'A Z':
        total += (2 + 6)
    elif data_list[i] == 'B X':
        total += (1 + 0)
    elif data_list[i] == 'B Y':
        total += (2 + 3)
    elif data_list[i] == 'B Z':
        total += (3 + 6)
    elif data_list[i] == 'C X':
        total += (2 + 0)
    elif data_list[i] == 'C Y':
        total += (3 + 3)
    elif data_list[i] == 'C Z':
        total += (1 + 6)
    else:
        break

print("Part Two")
print(total)
