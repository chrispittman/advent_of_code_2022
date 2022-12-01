import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
# data = [int(line) for line in data]

elves = [0]
for cal in data:
    if cal == '':
        elves.append(0)
    else:
        elves[-1] += int(cal)
print(max(elves))
