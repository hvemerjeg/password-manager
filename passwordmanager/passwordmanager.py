from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import sys
import sqlite3
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PasswordManager:
    def __init__(self, master_key:str, database:str, passfile:str):
        self.database = database
        self.master_key = master_key
        self.passfile = passfile
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()

    def createDefaultTable(self, random_string:str):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
        default(id INTEGER PRIMARY KEY, random_string text NOT NULL) 
        """)


    def savePassword(self, service:str, username:str, password:str) -> None:
        pass
