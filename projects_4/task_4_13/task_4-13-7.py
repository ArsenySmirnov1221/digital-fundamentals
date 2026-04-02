set = []

while True:
    inp = input()

    if inp == "":
        break

    inp = int(inp)
    set.append(inp)

sum = 0

for i in range(len(set)):
    sum += set[i]

print(sum/len(set))