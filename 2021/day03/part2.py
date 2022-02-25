with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#--------------------------------------------------------------------PART 2---------------------------------------------------------------------------
input = []
for line in lines:
    input.append(line.strip())

rates = {"oxygenGenerator": "", "O2scrubber": ""}

count0 = 0
count1 = 0

toDeleteGenerator = []


#---------------------------------------oxygenGenerator----------------------------
for i in range(len(input[0])):
    for binary in input:
        if binary[i] == "0":
            count0 += 1
        else:
            count1 += 1

    if count0 > count1:
        for binary in input:
            if binary[i] == "1":
                toDeleteGenerator.append(binary)
    
    elif count1 > count0:
        for binary in input:
            if binary[i] == "0":
                toDeleteGenerator.append(binary)
    else:
        for binary in input:
            if binary[i] == "0":
                toDeleteGenerator.append(binary)
    if len(input) == 1:
        break
    input = [x for x in input if x not in toDeleteGenerator]
    toDeleteGenerator = []
    
    count0 = 0
    count1 = 0

rates["oxygenGenerator"] = input[0]
#---------------------------------------O2scrubber----------------------------
input = []
for line in lines:
    input.append(line.strip())


count0 = 0
count1 = 0

toDeleteO2 = []

for i in range(len(input[0])):
    for binary in input:
        if binary[i] == "0":
            count0 += 1
        else:
            count1 += 1

    if count0 > count1:
        for binary in input:
            if binary[i] == "0":
                toDeleteO2.append(binary)
    
    elif count1 > count0:
        for binary in input:
            if binary[i] == "1":
                toDeleteO2.append(binary)
    else:
        for binary in input:
            if binary[i] == "1":
                toDeleteO2.append(binary)
    if len(input) == 1:
        break
    input = [x for x in input if x not in toDeleteO2]
    toDeleteO2 = []
    count0 = 0
    count1 = 0

rates["O2scrubber"] = input[0]

print(int(rates["oxygenGenerator"], 2) * int(rates["O2scrubber"], 2))