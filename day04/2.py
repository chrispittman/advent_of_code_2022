import sys

data = [line.rstrip().split(',') for line in sys.stdin.readlines()]

total = 0
for line in data:
    as1,as2 = line[0].split('-'), line[1].split('-')
    as1 = [int(x) for x in as1]
    as2 = [int(x) for x in as2]
    if as2[0] <= as1[0] and as1[0] <= as2[1]:
        total += 1
    elif as1[0] <= as2[0] and as2[0] <= as1[1]:
        total += 1
print(total)

