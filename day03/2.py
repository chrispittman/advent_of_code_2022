import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in range(len(data)//3):
    l1,l2,l3 = data[i*3], data[i*3+1], data[i*3+2]
    common = [c for c in l1 if c in l2 and c in l3][0]
    prio = priorities.find(common) + 1
    total += prio

print(total)
