import os
import base64
import signal
import sys
import logging
import argparse

from passwordmanager import DatabaseInitialization, PasswordManager, KeyGenerator

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def main():

    def flagNeedsflag(flag_name:str, *args) -> None:
        sys.stderr.write(f'{flag_name} needs {", ".join(args)} options\n')
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("--encrypt", help="Encrypt a new password to store it in the database", action="store_true")
    parser.add_argument("--decrypt", help="Decrypt a password from the database", action="store_true")
    parser.add_argument("--update-master-key", help="Change master key password and password file", action="store_true")
    parser.add_argument("--list-services", help="List services for which password exist (google, facebook, etc.)", action="store_true")
    parser.add_argument("--update", help="Update a password for a specific service", action="store_true")
    parser.add_argument("--delete", help="""Delete a password. The password will be held in a different table for recovery.
                        Will be eliminated after 30 days""", action="store_true")
    parser.add_argument("--recover", help="Recover a deleted password. Passwords are held in a different table for decovery for 30 days", action="store_true")
    parser.add_argument("--new-database", help="Create a new database file to save your passwords.", action="store_true")
    parser.add_argument("--database", help="Database file with passwords. File extension needs to end in pdbm")
    parser.add_argument("--passfile", help="""Passfile required (besides the password) to decrypt and encrypt database.
                        This file is the "something you have" factor. File extension needs to end in pdbmk""")
    parser.add_argument("--service", help="The service related to the password (google, facebook, etc.)")
    args = parser.parse_args()

    main_options = args.__dict__
    if not tuple(main_options.values()).count(True) > 0:
        parser.print_help()
        exit(1)

    if tuple(main_options.values()).count(True) > 1:
        options = tuple(filter(lambda x: x[1] == True, main_options.items()))
        options = [t[0] for t in options]
        sys.stderr.write(f'You can not use {", ".join(options)} options at the same time\n')
        exit(1)

    if args.new_database:
        if not (args.passfile and args.database):
            flagNeedsflag("--new-database", "--passfile", "--database")
        if not args.passfile.endswith(".pdbmk"):
            sys.stderr.write(f"File extension of passfile needs to end in .pdbmk\n")
            exit(1)
        if not args.database.endswith(".pdbm"):
            sys.stderr.write(f"File extension of databse needs to end in .pdbm\n")
            exit(1)
        password_manager = DatabaseInitialization(database_name=args.database).initDatabase()

if __name__ == "__main__":
    main()
