set = []

while True:
    inp = input()

    if inp == "":
        break

    inp = int(inp)
    set.append(inp)

sum_el = 0
sum_ind = 0

for i in range(len(set)):
    if i % 2 == 0:
        sum_el += set[i]
        sum_ind += 1

print(sum_el/sum_ind)

