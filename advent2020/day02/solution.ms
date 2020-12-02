passcount = 0
myPath = "input.txt"
fn checkpass1 minnum maxnum letter pass = 
(
    stripped = substituteString pass letter ""
    lettercount = (pass.count - stripped.count)
    if (lettercount <= maxnum and lettercount >= minnum) then (return 1) else (return 0)
)
fn checkpass2 indexA indexB letter pass =
(
    valid = 0
    if pass[indexA] == letter do (valid +=1) 
    if pass[indexB] == letter do (valid +=1)
    if valid == 1 then (return 1) else return 0
)
fs = openFile myPath mode:"r"
while not eof fs do(
    l = readline fs
	splittokens = filterString l ": "
	nums = filterString splittokens[1] "-"
	intA = nums[1] as Integer
	intB = nums[2] as Integer
	letter = splittokens[2]
	pass = splittokens[3]
    passcount += checkpass2 intA intB letter pass
)
close fs