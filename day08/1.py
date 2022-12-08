import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

y_max = len(data)
x_max = len(data[0])

total_vis = 0
for y in range(y_max):
    for x in range(x_max):
        vis_left = True
        for x1 in range(x):
            if data[y][x1] >= data[y][x]:
                vis_left = False
        vis_right = True
        for x1 in range(x+1,x_max):
            if data[y][x1] >= data[y][x]:
                vis_right = False
        vis_top = True
        for y1 in range(y):
            if data[y1][x] >= data[y][x]:
                vis_top = False
        vis_bottom = True
        for y1 in range(y+1,y_max):
            if data[y1][x] >= data[y][x]:
                vis_bottom = False
#        print (x,y,data[y][x],vis_left,vis_right,vis_top,vis_bottom)
        if vis_left or vis_right or vis_top or vis_bottom:
            total_vis += 1

print(total_vis)
