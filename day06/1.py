import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
line = data[0]

for i in range(4, len(line)+1):
    if len(set(line[i-4:i])) == 4:
        print (i)
        break
