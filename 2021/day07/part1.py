import statistics

with open("input.txt", "r") as f:
    lines = f.readlines()
    
input = []
for line in lines:
    input.append(line.strip())

#-------------------------------PART 1------------------------------------------------

positions = [int(x) for x in input[0].split(",")]

fuel = 0

# most efficient value to travel to
center = statistics.median(positions)

print(center)
for pos in positions:
    fuel += abs(pos - center)

print(int(fuel))