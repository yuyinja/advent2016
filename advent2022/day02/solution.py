import os, sys
from adventofcode.lib import utils

# loading data through a utility module
data = utils.loadInput("input.txt", dir=os.path.dirname(__file__), strip=True)

def solve(solutionPart):
    winPoints = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    resultMap = {"X": 0, "Y": 3, "Z": 6}

    # lambda function to quickly get the score
    shapePoints = lambda inputPlayer, offset: (int(ord((inputPlayer))) - offset)

    score = 0
    for line in data:
        # strips non letter characters out of line
        inputOpponent, inputPlayer = "".join(c for c in line if c.isalpha())[:2]

        player = inputPlayer

        # PART 2 SOLUTION
        if solutionPart == 2:
            # get the score you want through map
            resultTarget = resultMap[inputPlayer]
            # map index for values to get what needs to be played to get that score
            player = list(winPoints[inputOpponent].keys())[
                list(winPoints[inputOpponent].values()).index(resultTarget)
            ]

        # offset for xyz = 87, abc = 64
        score += shapePoints(player, 87)
        score += winPoints[inputOpponent][player]

    return score

print("SOLUTION PART 1: ", solve(1))
print("SOLUTION PART 2: ", solve(2))