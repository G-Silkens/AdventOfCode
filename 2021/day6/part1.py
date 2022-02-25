with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------

ageList = [int(x) for x in input[0].split(",")]

tempAges = []


for i in range(80):
    tempAges = []
    for age in ageList:
        if age == 0:
            tempAges.append(6)
            tempAges.append(8)
        else:
            tempAges.append(age - 1)
    ageList = tempAges

count = 0
for age in ageList:
    count += 1

print(count)