import copy
import numpy
import logging
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

from adventofcode.advent2019.lib import utils
logger = utils.logger
logger.setLevel(logging.INFO)

data = utils.loadInput("input.txt")
pathAdata = data[0].strip("\n").split(",")
pathBdata = data[1].strip("\n").split(",")

PATH_PROCESS = {"L": (-1,0), "R": (1,0), "U":(0,1), "D": (0,-1)}

class PathObject(object):
    
    def __init__(self, inputdata):
        self.units = [(0,0)]
        self.currentPos = (0,0)
        self.move(inputdata)
        
    def move(self, inputs):
        for input in inputs:
            dir = numpy.array(PATH_PROCESS[input[0]])
            units = int(input[1:])
            moved = (dir * units)
            self.currentPos += moved
            self.units.append(tuple(self.currentPos))
            
    @property
    def codes(self):
        codes = [mpath.Path.LINETO for x in self.units]
        codes[0] = mpath.Path.MOVETO
        return codes
    
pathA = PathObject(pathAdata)
pathB = PathObject(pathBdata)

fig, ax = plt.subplots()
ax.axis([-6000, 6000, -8000, 8000])
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
string_pathA = mpath.Path(pathA.units, pathA.codes)
patchA = mpatches.PathPatch(string_pathA, facecolor="none", lw=1, ec="red")

string_pathB = mpath.Path(pathB.units, pathB.codes)
patchB = mpatches.PathPatch(string_pathB, facecolor="none", lw=1, ec="blue")

ax.add_patch(patchA)
ax.add_patch(patchB)
plt.legend(['pathA', 'pathB'])
plt.show()

