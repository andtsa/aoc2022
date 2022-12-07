f = open("day2.txt", "r")
filein = f.read()
lines = filein.split("\n")
score = 0

# cheat sheet
# A,X = rock  B,Y = paper  C,Z = scissors
winningMoves = [["A", "Y"], ["B", "Z"], ["C", "A"]]
drawingMoves = [["A", "X"], ["B", "Y"], ["C", "Z"]]

count = 0
for line in lines:
    scoreBefore = score
    count += 1
    print("\nthis is move #" + str(count))
    moves = line.split(" ")
    if moves[1] == "X":
        score += 1
        print("played rock, +1")
    elif moves[1] == "Y":
        score += 2
        print("played paper, +2")
    elif moves[1] == "Z":
        score += 3
        print("played scissors, +3")

    move = [moves[0], moves[1]]
    if move in winningMoves:
        score += 6
        print("move "+moves[1] + " against "+moves[0]+" resulted in a win, +6")
    elif move in drawingMoves:
        score += 3
        print("move " + moves[1] + " against " + moves[0] + " resulted in a draw, +3")
    else:
        print("move " + moves[1] + " against " + moves[0] + " resulted in a loss, +0")

    print("Δscore = +" + str(score - scoreBefore))


print(score)