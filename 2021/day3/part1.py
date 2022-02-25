with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#--------------------------------------------------------------------PART 1---------------------------------------------------------------------------
rates = {"gamma": "", "epsilon": ""}
switchedInput = []
temp = ""

# switch input list around and put in switchedInput list [index1, index2, etc...]
for index in range(len(input[0])):
    for i in range(len(input)):
        temp += input[i][index]
    switchedInput.append(temp)
    temp = ""


count0 = 0
count1 = 0

for binary in switchedInput:
    for number in binary:
        if number == "0":
            count0 += 1
        else:
            count1 += 1

    if count0 > count1:
        rates["gamma"] += "0"
    else:
        rates["gamma"] += "1"
    count0 = 0
    count1 = 0

# reverse for epsilon
for value in rates["gamma"]:
    if value == "0":
        rates["epsilon"] += "1"
    else:
        rates["epsilon"] += "0"


print(int(rates["gamma"], 2) * int(rates["epsilon"], 2))