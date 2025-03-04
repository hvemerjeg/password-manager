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

    def savePassword(self, service:str, username:str, password:str) -> None:
        pass
