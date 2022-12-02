import sys

data = [line.rstrip().split() for line in sys.stdin.readlines()]

needed_outcomes = {"X":"lose", "Y":"draw", "Z":"win"}
shape_scores = {"rock":1,"paper":2,"scissors":3}
outcome_scores = {"lose":0, "draw":3, "win":6}
opp_plays = {
   "A":{"win":"paper","lose":"scissors","draw":"rock"},
   "B":{"win":"scissors","lose":"rock","draw":"paper"},
   "C":{"win":"rock","lose":"paper","draw":"scissors"},
}

total_score = 0
for play in data:
    outcome = needed_outcomes[play[1]]
    my_play = opp_plays[play[0]][outcome]
    shape_score = shape_scores[my_play]
    outcome_score = outcome_scores[outcome]
    total_score += shape_score + outcome_score

print(total_score)
