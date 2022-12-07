filein = input()
elves = filein.split("\n\n")
maxCalories = []
for elf in elves:
    calories = elf.split("\n")
    total = 0
    for cal in calories:
        total+=int(cal)
    maxCalories.append(total)

maxCalories.sort()

print(maxCalories[-1]+maxCalories[-2]+maxCalories[-3])
