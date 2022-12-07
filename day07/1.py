import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

cwd = []
dir_sizes = {}

for line in data:
     if line.startswith('$ cd'):
         newdir = line[5:]
         if newdir=='..':
             cwd = cwd[:-1]
         else:
             cwd.append(newdir)
     elif line.startswith('$ ls'):
         pass
     elif line.startswith('dir'):
         pass
     else:
         size,file = line.split(' ')
         for i in range(len(cwd)):
             cur_dir = '/'.join(cwd[:i+1])
             if cur_dir not in dir_sizes:
                 dir_sizes[cur_dir] = 0
             dir_sizes[cur_dir] += int(size)

total = 0
for size in dir_sizes.values():
    if (size<=100000):
        total += size
print (total)
