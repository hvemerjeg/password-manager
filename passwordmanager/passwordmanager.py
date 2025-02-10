from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import logging
import sys
import sqlite3
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PasswordManager:
    def __init__(self, master_key:str, filename=None):
        self.filename = filename
        self.master_key = master_key

    def initDatabase(self, filename:str):
        if self.filename == None:
            logging.info('Creating new database file Database.db')
            if not os.path.exists('./Database.db'):
                self.filename = 'Database.db'

    def savePassword(self, service:str, username:str, password:str) -> None:
        pass
