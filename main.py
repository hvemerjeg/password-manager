import os
import base64
import signal
import sys
import logging
import argparse

import passwordmanager

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', required=False)
    parser.add_argument('--passfile', required=False)

    args = parser.parse_args()
    if args.database and args.passfile:
        option = input('1)Get password\n2) Save new password\n3)Update a password\n4)Update master key\n5)Delete a password\n6)Recover a password\n')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '6':
            pass
        else:
            sys.stderr.write(f'Unrecognized option: {option}\n')
    else:
        option = input('Do you want to create a new database? (Y or N): ').upper()
        if option ==  'Y':
            pass
        elif option == 'N':
            pass
        else:
            sys.stderr.write(f'Unrecognized option: {option}\n')
if __name__ == '__main__':
    main()
