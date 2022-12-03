import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for line in data:
    s1,s2 = line[:len(line)//2], line[len(line)//2:]
    common = [c for c in s1 if c in s2][0]
    prio = priorities.find(common) + 1
    total += prio

print(total)
