import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

y_max = len(data)
x_max = len(data[0])

max_score = 0
for y in range(y_max):
    print("")
    for x in range(x_max):
        score_left = 0
        for x1 in range(x-1,-1,-1):
            score_left += 1
            if data[y][x1] >= data[y][x]:
                break
        score_right = 0
        for x1 in range(x+1,x_max):
            score_right += 1
            if data[y][x1] >= data[y][x]:
                break
        score_top = 0
        for y1 in range(y-1,-1,-1):
            score_top += 1
            if data[y1][x] >= data[y][x]:
                break
        score_bottom = 0
        for y1 in range(y+1,y_max):
            score_bottom += 1
            if data[y1][x] >= data[y][x]:
                break

        score = score_left * score_right * score_top * score_bottom
#        print (x,y,data[y][x],score,"*",score_left,score_right,score_top,score_bottom)
        max_score = max(score, max_score)

print(max_score)
