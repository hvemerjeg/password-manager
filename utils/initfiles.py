import logging
import os
import sys
from passwordmanager import PasswordManager

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class initFiles:
    def __init__(self):
        self.random_string = ""
        while len(self.random_string) < 16:
            for byte in os.urandom(32):
                if byte in range(32, 127):
                    self.random_string += chr(byte)

    def initFiles(component:str, db=False):
        if not os.path.exists(component):
            logger.info("Creating %s", component)
            try:
                if db:
                    with open(component, "w") as f:
                        pass
                else:
                    with open(component, "w") as f:
                        f.write(f"{self.random_string}\n")
            except PermissionError as e:
                sys.stderr.write(f"{e}\n")
                exit(1)
        else:
            logger.info("%s already exists", component)
