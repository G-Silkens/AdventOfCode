with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------

tempCoordinates = []
for line in input:
    tempCoordinates.append(line.replace(" ", "").split("->"))

coordinatePairs = []

for coordinate in tempCoordinates:
    coordinatePairs.append([coordinate[0].split(",")] + [coordinate[1].split(",")])

# not [[0] * x] * x because id's need to be unique
# adjust range to max size (or higher) of x and y
field = [[0 for i in range(1000)] for j in range(1000)]
# field = [[0 for i in range(10)] for j in range(10)]


for coordinates in coordinatePairs:
    x1 = min(int(coordinates[0][0]), int(coordinates[1][0]))
    y1 = min(int(coordinates[0][1]), int(coordinates[1][1]))

    x2 = max(int(coordinates[0][0]), int(coordinates[1][0]))
    y2 = max(int(coordinates[0][1]), int(coordinates[1][1]))

    # x is the same (horizontal)
    if x1 == x2:

        for i in range(y1, y2 + 1):
            field[i][x1] += 1
    
    # y is the same (vertical)
    elif y1 == y2:
        for i in range(x1, x2 + 1):
            field[y1][i] += 1
                

count = 0

for row in field:
    for num in row:
        if num > 1:
            count += 1
        print(num, end=" ")
    print()

print(count)