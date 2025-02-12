import os
import base64
import signal
import sys
import logging
import argparse

import passwordmanager

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--encrypt', help='Encrypt a new password to store it in the database', action='store_true')
    parser.add_argument('--decrypt', help='Decrypt a password from the database', action='store_true')
    parser.add_argument('--update-master-key', help='Change master key password and password file', action='store_true')
    parser.add_argument('--list-services', help='List services for which password exist (google, facebook, etc.)', action='store_true')
    parser.add_argument('--update', help='Update a password for a specific service', action='store_true')
    parser.add_argument('--delete', help='''Delete a password. The password will be held in a different table for recovery.
                        Will be eliminated after 30 days''', action='store_true')
    parser.add_argument('--recover', help='Recover a deleted password. Passwords are held in a different table for decovery for 30 days', action='store_true')
    parser.add_argument('--database', help='Database file with passwords. File extension needs to end in pdbm')
    parser.add_argument('--passfile', help='''Passfile required (besides the password) to decrypt and encrypt database.
                        This file is the 'something you have' factor. File extension needs to end in pdbmk''')
    parser.add_argument('--new-database', help='''Create a new database file to save your passwords.
    Provide only the path to the directory without filename''', action='store_true')
    parser.add_argument('--service', help='The service related to the password (google, facebook, etc.)')

    args = parser.parse_args()
if __name__ == '__main__':
    main()
