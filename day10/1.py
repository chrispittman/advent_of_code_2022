import sys
from itertools import chain

data = [line.rstrip().split(' ') for line in sys.stdin.readlines()]
args = chain.from_iterable(data)

cycle_num = 0
curr_instr = ""
x = 1

total_str = 0
for arg in args:
    cycle_num += 1
    if cycle_num in [20,60,100,140,180,220]:
        total_str += cycle_num * x
    if curr_instr=='addx':
        x += int(arg)
        curr_instr = ''
    elif arg=='addx':
        curr_instr = 'addx'
    elif arg=='noop':
        pass
print(total_str)
