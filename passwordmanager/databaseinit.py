import logging
import os
import sys
from utils import Singleton

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DatabaseInitialization(Singleton):
    def initDatabase(self):
        if not os.path.exists(self.database_name):
            logger.info("Creating database %s", self.database_name)
            try:
                with open(self.database_name, "w") as f:
                    pass
            except PermissionError as e:
                sys.stderr.write(f"{e}\n")
                exit(1)
