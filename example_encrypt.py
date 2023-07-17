"""
simple2encrypt.py
Script for encrypting a file using the Encryption class from utils.
"""
import argparse
import os
import sys

from simple2encrypt import read_binary, Encryption, write_binary

parser = argparse.ArgumentParser(prog='encrypt file use AES encryption', description='take file path and key path and '
                                                                                     'encrypt the file use the key')
parser.add_argument('file_path', help='file path')
parser.add_argument('key_path', help='key path to encrypt the file_path')

args = parser.parse_args()


def main(file_path):
    """
    Encrypt a file using the Encryption class.
    """
    file_path = args.file_path
    key_path = args.key_path
    new_path = file_path + '.enc'

    try:
        # Read the encryption key from the file
        key = read_binary(key_path)

        # Read binary data from the file path
        data = read_binary(file_path)
    except (FileNotFoundError, ValueError, PermissionError) as read_error:
        print(f"Error reading file: {read_error}")
        sys.exit()

    # Encrypt the data
    encrypt = Encryption(key, data)
    encrypted_data = encrypt.encrypt()

    # Write the encrypted data to a new file
    try:
        write_binary(new_path, encrypted_data)
    except (ValueError, PermissionError) as write_error:
        print(f"Error writing file: {write_error}")
        sys.exit()

    # Remove the original file
    try:
        os.remove(file_path)
    except (PermissionError, FileNotFoundError) as remove_error:
        print(f"Error removing file: {remove_error}")
        sys.exit()

    print(f'Encryption completed encrypted file save at {new_path}')


if __name__ == '__main__':
    main()
