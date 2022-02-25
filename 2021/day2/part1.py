with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------
directions = {"horizontal": 0, "depth": 0,}

for move in input:
    if move.split()[0] == "forward":
        directions["horizontal"] += int(move.split()[1])
    if move.split()[0] == "down":
        directions["depth"] += int(move.split()[1])
    if move.split()[0] == "up":
        directions["depth"] -= int(move.split()[1])

print(directions["horizontal"] * directions["depth"])