import os, sys
from adventofcode.lib import utils

data = utils.loadInput("input.txt", dir=os.path.dirname(__file__))
data = sorted(set([int(x) for x in data]))

def solution01(data):
    for x in data:
        if (2020 - x) in data:
            print("Solution 1: ", ((2020 - x) * x))

def solution02(data):
    for i in range(len(data)):
        checkdata = data.copy()
        base = data[i]
        recursiveCheck(base, checkdata[i+1:])

def recursiveCheck(base, data):
    # get rid of impossibly large numbers by adding
    # lowest 2 numbers from there - and removing anything higher than the remain
    minval = 2020 - base - data[0]
    if minval in data:
        # print (base, minval, data)
        print ("Solution 2: ", base * data[0] * minval)
        sys.exit(0)
    else:
        data = [x for x in data if x <= minval]
        if len(data) > 1:
            recursiveCheck(base, data[1:])
            
solution01(data)
solution02(data)

