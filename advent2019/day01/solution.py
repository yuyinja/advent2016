from advent2019.lib import utils
from advent2019.lib.utils import logger
import logging
logger.setLevel(logging.INFO)

data = utils.loadInput("input.txt")
data = [float(x) for x in data]
if not data :
    logger.error("No valid input data")

def getFuelReq(input):
    fuelreq = int(input / 3) - 2
    return fuelreq

def solutionPart1(inputs):
    fuel = 0

    for input in inputs :
        fuelreq = getFuelReq(input)
        fuel += fuelreq

        return fuel

def solutionPart2(inputs):
    fuel = 0

    for input in inputs:
        fuelreq = input
        logger.debug("\n")
        while fuelreq > 0:
            fuelreq = getFuelReq(fuelreq)
            if fuelreq > 0:
                fuel += fuelreq
            logger.debug("fuel: {} | fuelreq: {}".format(fuel, fuelreq))

    return fuel

print solutionPart2(data)