import os

# adding the loadInput function for learning reference
def loadInput(fp, dir=None, strip=True):
    # checks if directory exists
    if dir:
        # if so creates the filepath
        fp = os.path.join(dir, fp)
    # if file exists
    if os.path.exists(fp):
        # open the file, read only
        with open(fp, "r") as f:
            all = f.readlines()
            # if chosen to strip, strip out new line calls from end of each line
            if strip:
                all = [x.strip("\n") for x in all]
            return all
    # if file doesn't exist, return nothing
    else:
        return None