import logging
import os
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class DatabaseInit:
    @classmethod
    def initDatabase(cls, database_name:str):        
        if not os.path.exists(database_name):
            logging.info('Creating database %s', database_name)
            try:
                with open(database_name, 'w') as f:
                    pass
            except PermissionError as e:
                sys.stderr.write(f'{e}\n')
                exit(1)
