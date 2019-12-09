import copy
import numpy as np
import logging
from shapely.geometry import LineString

from adventofcode.advent2019.lib import utils

logger = utils.logger
logger.setLevel(logging.INFO)

data = utils.loadInput("input.txt")
pathAdata = data[0].strip("\n").split(",")
pathBdata = data[1].strip("\n").split(",")

PATH_PROCESS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


class PathObject(object):
    def __init__(self, inputdata):
        self.units = [(0, 0)]
        self.currentPos = (0, 0)
        self.move(inputdata)

    def move(self, inputs):
        for input in inputs:
            dir = np.array(PATH_PROCESS[input[0]])
            units = int(input[1:])
            moved = (dir * units)
            self.currentPos += moved
            self.units.append(tuple(self.currentPos))


pathA = PathObject(pathAdata)
pathB = PathObject(pathBdata)

lineA = LineString(pathA.units)
lineB = LineString(pathB.units)

intersections = lineA.intersection(lineB)
intersections = sorted(intersections, key=lambda x: (abs(x.x) + abs(x.y)))
print abs(intersections[1].x) + abs(intersections[1].y)