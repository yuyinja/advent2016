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
        self.inputs = inputdata
        self.units = [(0, 0)]
        self.currentPos = (0, 0)
        self.move()

    def move(self):
        for input in self.inputs:
            dir = np.array(PATH_PROCESS[input[0]])
            units = int(input[1:])
            moved = (dir * units)
            self.currentPos += moved
            self.units.append(tuple(self.currentPos))

    def lengthToIntersection(self, intersection):
        pos = (0,0)
        length = 0
        for input in self.inputs:
            dir = np.array(PATH_PROCESS[input[0]])
            units = int(input[1:])
            unitsCovering = [tuple((dir * i) + pos) for i in range(units)]
            if intersection in unitsCovering:
                add = unitsCovering.index(intersection)
                length += add
                return length
            moved = (dir * units)
            pos += moved
            length += units

pathA = PathObject(pathAdata)
pathB = PathObject(pathBdata)

lineA = LineString(pathA.units)
lineB = LineString(pathB.units)
intersections = lineA.intersection(lineB)

def partA(intersections):
    intersections = sorted(intersections, key=lambda x: (abs(x.x) + abs(x.y)))
    return (abs(intersections[1].x) + abs(intersections[1].y))

def partB(intersections):
    intersections = [tuple((x.x, x.y)) for x in intersections]
    intersections = sorted(intersections, key=lambda intersection:(pathB.lengthToIntersection(intersection) + pathA.lengthToIntersection(intersection)))

    return (pathB.lengthToIntersection(intersections[1])+ pathA.lengthToIntersection(intersections[1]))