import re

def checkCons(str):
    for i in range(5, 0, -1):
        if int(str[i]) >= int(str[i-1]):
            continue
        else:
            return 0

    return 1

def filterDoubles(str):
    doubles = sorted(set(re.findall(r"([0-9])\1",  str)))
    for digit in doubles:
        if str.count(digit) == 2:
            return 1

    return 0

input = "156218-652527"
inputMin, inputMax = [int(x) for x in input.split("-")]

def solutionPartA():
    doubles = [str(i) for i in range(inputMin, inputMax) if re.findall(r"([0-9])\1", str(i))]
    singles = [x for x in doubles if checkCons(x)]
    return singles

def solutionPartB():
    filtered = solutionPartA()
    partB = [x for x in filtered if filterDoubles(x)]
    print len(partB)

# Dirty regex solution

# regexPart1 = r"^(?=1*2*3*4*5*6*7*8*9*$).*(.)(?<!(?=\1)..)\1"
# regexPart2 = r"^(?=1*2*3*4*5*6*7*8*9*$).*(.)(?<!(?=\1)..)\1(?!\1)"
#
# print "part1: ", len([str(i) for i in range(inputMin, inputMax) if re.findall(regexPart1, str(i))])
# print "part2: ", len([str(i) for i in range(inputMin, inputMax) if re.findall(regexPart2, str(i))])
