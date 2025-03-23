import logging
import os
import sys
from utils import Singleton

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DatabaseInitialization(Singleton):
    def initDatabase(self):
        if not os.path.exists(self.database_name):
            logging.info('Creating database %s', self.database_name)
            try:
                with open(self.database_name, 'w') as f:
                    pass
            except PermissionError as e:
                sys.stderr.write(f'{e}\n')
                exit(1)
