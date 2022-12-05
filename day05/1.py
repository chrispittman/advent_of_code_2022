import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

# Break input into lines describing the stacks, and the list of instructions
delim_posn = data.index("")
stack_lines = data[:delim_posn]
instr_lines = data[delim_posn+1:]

# Parse out the stack descriptions into the stacks, represented as a hash of boxes, first=top of stack
stacks = {}
for posn in range(len(stack_lines[-1])):
     posn_label = stack_lines[-1][posn]
     if (posn_label == " "):
         continue
     stack = []
     for stack_line in stack_lines[:-1]:
         if posn <= len(stack_line) and stack_line[posn] != " ":
             stack.append(stack_line[posn])
     stacks[posn_label] = stack

# parse out and follow the instructions
for instr in instr_lines:
    _,num_to_move,_,source,_,dest = instr.split(" ")
    for _ in range(int(num_to_move)):
        stacks[dest].insert( 0, stacks[source].pop(0) )

# print the top box on each stack
stack_tops = [stacks[k][0] for k in stacks if len(stacks[k])!=0]
print("".join(stack_tops))
