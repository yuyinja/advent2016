import os
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)

def loadInput(fp):
    if os.path.exists(fp):
        with open(fp, 'r') as f:
            all = f.readlines()
            return all
    else:
        return None

