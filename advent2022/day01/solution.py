import os, sys
from adventofcode.lib import utils

# loading data through a utility module
data = utils.loadInput("input.txt", dir=os.path.dirname(__file__), strip=True)

# initialize a dictionary
elfDict = {}
# make sure first elf is 1 and not 0 :)
elf = 1
# loop through each line
for line in data:
    # if its a blank line, its a new elf!
    if not line:
        # increases elf index by 1
        elf += 1
        # sets the value to 0, so we're not trying to int a null
        line = 0
    # checks if the elf exists, if it does, get the value, if not initialize the entry to 0
    total = elfDict.setdefault(elf, 0)
    # increase the total with the line value
    elfDict[elf] += int(line)

def solutionPart1(elfDict):
    print("PART 1 SOLUTION")
    # get max value
    print("MAX: ", max(elfDict.values()))
    # EXTRA: (I didn't read the question properly) get the max value from the dictionary, but get the key (elf index) instead of the value
    print("ELF CARRYING MOST: ", max(elfDict, key=elfDict.get))

def solutionPart2(elfDict):
    print("PART 2 SOLUTION")
    # sort all values
    sortedCalories = sorted(elfDict.values())
    # reverse it, so its highest first
    sortedCalories.reverse()
    # add up to 3 values
    print("SUM TOP 3: ", sum(sortedCalories[:3]))

solutionPart1(elfDict)
print("")
solutionPart2(elfDict)