import copy
import numpy

from advent2019.lib import utils
logger = utils.logger
logger.setLevel(logging.INFO)

data = utils.loadInput("input.txt")
data = [int(x) for x in (data[0].strip("\n").split(","))]
if not data :
    logger.error("No valid input data")

class Solution(object):
    PROCESS = {1: lambda x, y: x + y, 2: lambda x, y: x * y}

    def __init__(self, inputs):
        self.inputs = inputs

    @property
    def getInputs(self):
        return self.inputs

    def runA(self):
        i = 0
        while i >= 0:
            i = self.runProcess(i)

    def runProcess(self, i):
        input = self.inputs[i]
        if input != 99:
            if input in self.PROCESS.keys():
                indexX, indexY = [self.inputs[i+1], self.inputs[i+2]]
                x = self.inputs[indexX]
                y = self.inputs[indexY]
                loc = self.inputs[i+3]
                result = self.PROCESS[input](x, y)
                self.inputs[loc] = result
                return (i + 4)

        else:
            return -1

output = None
for arr in [(x, y) for x in range(100) for y in range(100)]:
    newdata = copy.copy(data)
    newdata[1] = arr[0]
    newdata[2] = arr[1]
    solution = Solution(newdata)
    solution.run()
    output = solution.getInputs[0]
    if output == 19690720:
        print arr, "result:", (100*arr[0]) + arr[1]
        break
    del(solution)

