import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
line = data[0]

pattern_length = 14
for i in range(pattern_length, len(line)+1):
    if len(set(line[i-pattern_length:i])) == pattern_length:
        print (i)
        break
