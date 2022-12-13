import sys
from math import floor

data = [line.rstrip() for line in sys.stdin.readlines()]

monkeys = {}

cur_monkey = 0
for line in data:
    parts = line.split(' ')
    if len(parts)==1:
        pass
    elif parts[0] == 'Monkey':
        cur_monkey = parts[1][:-1]
        monkeys[cur_monkey] = {'num_inspections':0}
    elif parts[2] == 'Starting':
        monkeys[cur_monkey]['items'] = [int(x.replace(',','')) for x in parts[4:]]
    elif parts[2] == 'Operation:':
        monkeys[cur_monkey]['operation'] = parts[6:8]
    elif parts[2] == 'Test:':
        monkeys[cur_monkey]['test'] = int(parts[5])
    elif parts[5] == 'true:':
        monkeys[cur_monkey]['true'] = parts[9]
    elif parts[5] == 'false:':
        monkeys[cur_monkey]['false'] = parts[9]

for round in range(20):
    print("")
    print("")
    print ("round ", round+1)
    print (monkeys)
    for m_ix,monkey in monkeys.items():
        while len(monkey['items']) > 0:
            monkey['num_inspections'] += 1
            item = monkey['items'].pop(0)
            worry_incr = item if monkey['operation'][1]=='old' else int(monkey['operation'][1])
            if monkey['operation'][0] == '+':
                item += worry_incr
            elif monkey['operation'][0] == '*':
                item *= worry_incr
            item = floor(item/3)
            divisible = item % monkey['test'] == 0
            monkey_to_throw_to = monkey['true'] if divisible else monkey['false']
            monkeys[monkey_to_throw_to]['items'].append(item)

insps = sorted([m['num_inspections'] for m in monkeys.values()])
print(insps[-1] * insps[-2])
