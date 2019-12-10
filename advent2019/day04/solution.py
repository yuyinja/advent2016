import re

input = "156218-652527"
inputMin, inputMax = [int(x) for x in input.split("-")]

regexPart1 = r"^(?=1*2*3*4*5*6*7*8*9*$).*(.)(?<!(?=\1)..)\1"
regexPart2 = r"^(?=1*2*3*4*5*6*7*8*9*$).*(.)(?<!(?=\1)..)\1(?!\1)"

print "part1: ", len([str(i) for i in range(inputMin, inputMax) if re.findall(regexPart1, str(i))])
print "part2: ", len([str(i) for i in range(inputMin, inputMax) if re.findall(regexPart2, str(i))])