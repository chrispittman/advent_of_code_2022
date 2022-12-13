import sys
import json
from functools import cmp_to_key

data = [line.rstrip() for line in sys.stdin.readlines()]

ORDER_TRUE=-1
ORDER_FALSE=1
ORDER_UNKNOWN=0

def compare(l1,l2):
    if isinstance(l1,int) and isinstance(l2,int):
        if l1==l2:
            return ORDER_UNKNOWN
        elif l1<l2:
            return ORDER_TRUE
        else:
            return ORDER_FALSE
    if isinstance(l1,int):
        l1 = [l1]
    if isinstance(l2,int):
        l2 = [l2]
    max_l = max(len(l1), len(l2))
    for posn in range(max_l):
        if posn>=len(l1):
            return ORDER_TRUE
        elif posn>=len(l2):
            return ORDER_FALSE
        else:
            comp = compare(l1[posn],l2[posn])
            if comp in [ORDER_TRUE,ORDER_FALSE]:
                return comp

all_lines = [ [[2]], [[6]] ]
for ix in range(len(data)//3 + 1):
    line1 = json.loads(data[ix*3])
    line2 = json.loads(data[ix*3+1])
    all_lines.append(line1)
    all_lines.append(line2)
all_lines_sorted = sorted(all_lines, key=cmp_to_key(compare))

posn1 = all_lines_sorted.index([[2]])+1
posn2 = all_lines_sorted.index([[6]])+1

print(posn1*posn2)
