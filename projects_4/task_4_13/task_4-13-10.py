set = []

while True:
    inp = input()

    if inp == "":
        break

    inp = int(inp)
    set.append(inp)

sum = 0

for i in range(len(set)):
    if i % 2 != 0:
        sum += set[i]

print(sum)