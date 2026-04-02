set = []
setsq = []
sum = 0

while True:
    inp = input()

    if inp == "":
        break

    inp = int(inp)
    set.append(inp)

for i in range(len(set)):
    setsq.append((set[i]) * (set[i]))

for i in range(len(setsq)):
    sum += setsq[i]

print(sum)