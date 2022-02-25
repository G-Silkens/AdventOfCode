with open("testinput.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#--------------------------------PART 2------------------------------------------------

lines = []
for ele in input:
    lines.append(ele)

result = {}
for line in lines:
    code, output = line.split(" | ")
    result[1] = [digit for digit in output if len(digit) == 2]
    result[4] = [digit for digit in output if len(digit) == 4]
    result[7] = [digit for digit in output if len(digit) == 3]
    result[8] = [digit for digit in output if len(digit) == 7]


print(result)