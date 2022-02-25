from collections import Counter, defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 2------------------------------------------------
ageList = Counter([int(x) for x in input[0].split(",")])


for _ in range(256):
    tempAges = defaultdict(int)
    for age, amount in ageList.items():
        if age == 0:
            tempAges[6] += amount
            tempAges[8] += amount
        else:
            tempAges[age - 1] += amount
    ageList = tempAges

print(sum(ageList.values()))