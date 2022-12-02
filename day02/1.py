import sys

data = [line.rstrip().split() for line in sys.stdin.readlines()]

shape_scores = {"X":1, "Y":2, "Z":3}
outcome_scores = {"lose":0, "draw":3, "win":6}
outcomes = {
   "A":{"X":"draw","Y":"win","Z":"lose"},
   "B":{"X":"lose","Y":"draw","Z":"win"},
   "C":{"X":"win","Y":"lose","Z":"draw"},
}

total_score = 0
for play in data:
    outcome = outcomes[play[0]][play[1]]
    shape_score = shape_scores[play[1]]
    outcome_score = outcome_scores[outcome]
    total_score += shape_score + outcome_score

print(total_score)
