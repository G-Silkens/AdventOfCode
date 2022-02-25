with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 2------------------------------------------------

def checkBingoLastBoard(finalBoards, pickedNumbers, index):
    finalBoardNumbers = []
    # get answer if there's 1 board left
    if len(finalBoards) == 1:
        for line in finalBoards[index]:
            for num in line:
                finalBoardNumbers.append(num)
        finalBoardNumbers = [int(x) for x in finalBoardNumbers if int(x) not in pickedNumbers]
        print(pickedNumbers)
        print(sum(finalBoardNumbers) * int(pickedNumbers[-1]))
        quit()


numbers = input[0].split(",")
numbers = [int(i) for i in numbers]

boards = input[2:]

boards = [i for i in boards if i != ""]

boardlists = []

for i in range(0, len(boards), 5):
    boardlists.append(boards[i:i + 5])

intBoardLines = []

for board in boardlists:
    for line in board:
        intBoardLines.append(line.split())

finalBoards = []

for i in range(0, len(intBoardLines), 5):
    finalBoards.append(intBoardLines[i:i + 5])
    
pickedNumbers = []
foundBingo = False

for num in numbers:
    print(num)
    pickedNumbers.append(num)
    
    # loop through boards to a find bingo
    for index in range(len(finalBoards) - 1, -1, -1):
                
        # check rows for bingo
        for row in finalBoards[index]:
            row = {int(i) for i in row}

            if row.issubset(pickedNumbers):
                checkBingoLastBoard(finalBoards, pickedNumbers, index)
                # remove this board if bingo is found
                finalBoards.remove(finalBoards[index])

                foundBingo = True
                break

        if foundBingo:
            foundBingo = False
            continue

        # check columns for bingo
        boardColumn = []
        for i in range(len(finalBoards[0][0])):
            boardColumn = [row[i] for row in finalBoards[index]]
            boardColumn = {int(i) for i in boardColumn}

            if boardColumn.issubset(pickedNumbers):
                checkBingoLastBoard(finalBoards, pickedNumbers)
                # remove this board if bingo is found
                finalBoards.remove(finalBoards[index])
                break
