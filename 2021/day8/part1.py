with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------

tempSegments = []
for ele in input:
    tempSegments.append(ele.split(" | "))

segments = []
for i in range(len(tempSegments)):
    segments.append(tempSegments[i][1])

digits1478 = 0

for segment in segments:
    for digit in segment.split():
        if len(digit) == 2:
            digits1478 += 1

        elif len(digit) == 3:
            digits1478 += 1
        
        elif len(digit) == 4:
            digits1478 += 1

        elif len(digit) == 7:
            digits1478 += 1

print(digits1478)