import copy
import numpy
import logging

from adventofcode.advent2019.lib import utils

logger = utils.logger
logger.setLevel(logging.WARNING)

data = utils.loadInput("input.txt")[0]
if not data :
    logger.error("No valid input data")

def solution(input, phases, partB=False):
    logger.info("START INPUT: {}".format(input))
    if partB:
        baseoffset = [int(x) for x in str(input)[:7]]
        input = str(input)[7:]*10000
    else:
        baseoffset = [0, 1, 0, -1]
        input = str(input)
    for k in range(phases):
        inputlen = len(input)
        newinput = ""
        for i in range(inputlen):
            basepattern = [x for x in baseoffset for j in range(i+1)]
            logger.debug("phase: {}, line: {}, input: {} | {}".format(k, i, input, basepattern))
            logger.debug("basepattern indices : {}".format([(i+1) % len(basepattern) for i in range(inputlen)]))
            element =  str(sum([int(input[i]) * basepattern[((i+1) % len(basepattern))] for i in range(inputlen)]))[-1]
            newinput += element
        input = newinput
        logger.info("PHASE: {}, INPUT: {}".format(k, input))

    return input[:8]

#print #solution(data, 100, True)