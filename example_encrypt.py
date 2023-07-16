"""
encrypt.py
Script for encrypting a file using the Encryption class from utils.
"""

import os
import sys
from encryption_utils import read_binary, Encryption, write_binary


def main(file_path):
    """
    Encrypt a file using the Encryption class.
    """
    file_path = file_path
    encrypted_file_path = file_path + '.enc'

    try:
        # Read the encryption key from the file
        key = read_binary('my-key')

        # Read binary data from the file path
        data = read_binary(file_path)
    except (FileNotFoundError, ValueError, PermissionError) as read_error:
        print(f"Error reading file: {read_error}")
        sys.exit(1)

    # Encrypt the data
    encryption_obj = Encryption(key, data)
    encrypted_data = encryption_obj.encrypt()

    # Write the encrypted data to a new file
    try:
        write_binary(encrypted_file_path, encrypted_data)
    except PermissionError as write_error:
        print(f"Error writing file: {write_error}")
        sys.exit(1)

    # Remove the original file
    try:
        os.remove(file_path)
    except OSError as remove_error:
        print(f"Error removing file: {remove_error}")
        sys.exit(1)

    print('Encryption completed.')


if __name__ == '__main__':
    main('newfile.jpg')
