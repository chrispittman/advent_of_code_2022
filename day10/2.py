import sys
from itertools import chain

data = [line.rstrip().split(' ') for line in sys.stdin.readlines()]
args = chain.from_iterable(data)

cycle_num = 0
curr_instr = ""
x = 1
output = ""

for arg in args:
    horiz_posn = cycle_num % 40
    if horiz_posn - x in [-1,0,1]:
        output += '#'
    else:
        output += '.'
    cycle_num += 1
    if curr_instr=='addx':
        x += int(arg)
        curr_instr = ''
    elif arg=='addx':
        curr_instr = 'addx'
    elif arg=='noop':
        pass

for y in range(6):
    offset = y*40
    print(output[offset:offset+40])
