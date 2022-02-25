with open("input.txt", "r") as f:
    input = list(map(int, f.readlines()))

#-------------------------------PART 1------------------------------------------------
counter = 0

for i in range(len(input) -1):
    if int(input[i]) < int(input[i + 1]):
        counter += 1

print(counter)