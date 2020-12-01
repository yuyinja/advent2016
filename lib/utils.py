import os
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)

def loadInput(fp, dir=None, strip=True):
    if dir:
        fp = os.path.join(dir, fp)
    if os.path.exists(fp):
        with open(fp, 'r') as f:
            all = f.readlines()
            if strip:
                all = [x.strip("\n") for x in all]
            return all
    else:
        return None

