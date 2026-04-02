set = []

while True:
    inp = input()

    if inp == "":
        break

    inp = int(inp)
    set.append(inp)

potential_max = -9999999

for i in range(0, len(set)):
    if set[i] > potential_max:
        potential_max = set[i]

print(potential_max)