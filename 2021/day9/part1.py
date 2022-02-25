with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------

lowPoints = []

for i in range(len(input)):
    for j in range(len(input[0])):
        # check element above
        try:
            # if on top row set to True
            if i == 0:
                upIsHigher = True
            else:
                upIsHigher = input[i][j] < input[i - 1][j]
        except:
            upIsHigher = True
        
        # check element below
        try:
            # if on bottom row, set to true
            if i == len(input) - 1:
                downIsHigher = True
            else:
                downIsHigher = input[i][j] < input[i + 1][j]
        except:
            downIsHigher = True

        # check element to the left
        try:
            # if on first column, set to true
            if j == 0:
                leftIsHigher = True
            else:
                leftIsHigher = input[i][j] < input[i][j - 1]
        except:
            leftIsHigher = True
        
        # check element on the right
        try:
            # if on last column, set to true
            if j == len(input[0]) - 1:
                rightIsHigher = True
            else:
                rightIsHigher = input[i][j] < input[i][j + 1]
        except:
            rightIsHigher = True

        if upIsHigher and downIsHigher and leftIsHigher and rightIsHigher:
            lowPoints.append(input[i][j])

result = sum([int(x) + 1 for x in lowPoints])

print(result)