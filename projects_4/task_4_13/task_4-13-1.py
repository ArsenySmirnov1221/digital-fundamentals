set = [5, 4, -1, 0]


if set[0] > set[1]:
    min1 = set[1]
elif set[0] <= set[1]:
    min1 = set[0]

if set[2] > set[3]:
    min2 = set[3]
elif set[2] <= set[3]:
    min2 = set[2]

if min1 < min2:
    print(min1)
elif min1 > min2:
    print(min2)
