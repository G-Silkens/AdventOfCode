with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------
brackets = {"()": [], "[]": [], r"{}": [], "<>": []}

print(brackets.keys())

for line in input:
    brackets = brackets = {"()": [], "[]": [], r"{}": [], "<>": []}
    for char in line:
        for bracket in brackets.keys():
            if char in bracket:
                brackets[bracket] += char

print(brackets)
