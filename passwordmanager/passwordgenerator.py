import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class KeyGenerator:
    def __init__(self):
        self.__min_length = 16
        self.__master_key = '' # Should this be private?

    def generateKey(self) -> str:
        logger.info("Generating master_key")
        while len(self.__master_key) < 16:
            random_bytes = os.urandom(32)
            for byte in random_bytes:
                if byte in range(33, 127) and len(self.__master_key) < 16:
                    self.__master_key += chr(byte)
        return self.__master_key
