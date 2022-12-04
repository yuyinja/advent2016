import os
from adventofcode.lib import utils

# loading data through a utility module
data = utils.loadInput("input.txt", dir=os.path.dirname(__file__), strip=True)

#  function to get priority of shared item
def getPriority(x):
    # 96 lower, 38 upper (base 64 but starting from 27)
    base = 96
    if x.isupper():
        base = 38

    # get's ord which is unicode number for the letter, then we remove the base to turn it into the right points
    return (int(ord(x)) - base) 

def solve(data, solvePart):
    sum = 0

    if solvePart == 1:
        for line in data:
            # work out halfway point using length of line and converts to int for indexing
            halfway  = int(len(line)/2)
            # gets the two compartment items using halfway point
            firstC, secondC = [line[:halfway], line[halfway:]]
            # using set intersection to get the shared item (it will check what exists in a set for both lists)
            shareItem = list(set(firstC).intersection(secondC))[0]
            priority = getPriority(shareItem)
            sum += priority
    else:
        # iterate up by 3, up to the amount of lines in the input
        for i in range(0, len(data), 3):
            # starting on the 0, 3, 6 etc. iterate through 3 times
            checkLists = []
            for j in range(i, i+3):
                checkLists.append(set(data[j]))
            # another version of intersection, instead here we used a list of sets
            shareItem = list(set.intersection(*checkLists))[0]
            priority = getPriority(shareItem)
            sum += priority

    return sum


print("SOLUTION PART 1: ", solve(data, 1))
print("SOLUTION PART 2: ", solve(data, 2))