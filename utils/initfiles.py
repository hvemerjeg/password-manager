import logging
import os
import sys
from utils import Singleton

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def initFiles(component:str):
    if not os.path.exists(component):
        logger.info("Creating %s", component)
        try:
            with open(component, "w") as f:
                pass
        except PermissionError as e:
            sys.stderr.write(f"{e}\n")
            exit(1)
    else:
        logger.info("%s already exists", component)
