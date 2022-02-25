with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 2------------------------------------------------
#-----------------VERY SLOW SOLUTION NEEDS REFACTORING--------------------------------

positions = [int(x) for x in input[0].split(",")]

fuel = 0
fuelNeeded = 0
fuelNeededArr = []

toMove = 0

# most efficient value to travel to 
for i in range(max(positions) + 1):
    print(i)
    fuel = 0
    for pos in positions:
        toMove = 0
        toMove = abs(pos - i)

        for j in range(1, toMove + 1):
            fuel += j
            
    fuelNeededArr.append(fuel)


center = fuelNeededArr.index(sorted(fuelNeededArr)[0])
fuel = 0
toMove = 0

print(center)
for pos in positions:
    toMove = 0
    toMove = abs(pos - center)

    for i in range(1, toMove + 1):
        fuel += i

print(int(fuel))