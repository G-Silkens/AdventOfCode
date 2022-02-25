with open("input.txt", "r") as f:
    input = list(map(int, f.readlines()))

#-------------------------------PART 2------------------------------------------------
counter = 0

for i in range(len(input) -3):
    if int(input[i]) + int(input[i + 1]) + int(input[i + 2]) < int(input[i + 1]) + int(input[i + 2]) + int(input[i + 3]):
        counter += 1

print(counter)