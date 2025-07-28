from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import sys
import sqlite3
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PasswordManager:
    def __init__(self, master_key:str, filename=None):
        self.filename = filename
        self.master_key = master_key

    def savePassword(self, service:str, username:str, password:str) -> None:
        pass
