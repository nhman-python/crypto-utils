"""
encryption_utils.py
Utility functions for encryption and file operations.
"""

import argparse
import os
import sys
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad


class Encryption:
    """
    A class for performing encryption and decryption using the AES algorithm.
    """

    def __init__(self, key, data):
        """
        Initialize the Encryption object with the key and data.
        :param key: Encryption key
        :param data: Data to be encrypted or decrypted
        """
        self.key = key
        self.data = data

    def encrypt(self):
        """
        Encrypt the data using the AES algorithm.
        :return: Encrypted data
        """
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(self.data, cipher.block_size))
        return cipher.iv + encrypted_data

    def decrypt(self):
        """
        Decrypt the data using the AES algorithm.
        :return: Decrypted data
        """
        initialization_vector = self.data[:AES.block_size]  # Extract the IV from the data
        cipher = AES.new(self.key, AES.MODE_CBC, iv=initialization_vector)
        decrypted_data = cipher.decrypt(self.data[AES.block_size:])
        return unpad(decrypted_data, cipher.block_size)


def delete_extension(path: str) -> str:
    """
    Remove the file extension from a path.
    :param path: The file path
    :return:  without the extension
    """
    return path[:-4]


def create_new_key(password: str, path_key: str, length: int) -> str:
    """
    Create a new key based on the password and save it to a file.
    :param password: Password for key generation
    :param path_key: Path to save the key file
    :param length: Length key
    :return: Path of the new key file
    """
    if os.path.exists(path_key):
        raise FileExistsError('Key file already exists!')
    valid_lengths = [16, 24, 32]
    if length not in valid_lengths:
        raise ValueError('Invalid key length. Choose length from this list: [16, 24, 32]')
    with open(path_key, 'wb') as file:
        salt = os.urandom(length)
        key = PBKDF2(password, salt, dkLen=32)
        file.write(key)
        return path_key


def read_binary(file_path: str) -> bytes:
    """
    Read binary data from a file.
    :param file_path: Path of the file
    :return: Binary data from the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    if os.path.isdir(file_path):
        raise ValueError("Path is a directory. File path is expected.")
    with open(file_path, 'rb') as file:
        return file.read()


def write_binary(file_path, data):
    """
    Write binary data to a file.
    :param file_path: Path of the file to write the data to
    :param data:  write
    :return: True if the file was saved successfully
    """
    if os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' already exists.")
    if os.path.isdir(file_path):
        raise ValueError("Path is a directory. File path is expected.")
    with open(file_path, 'wb') as file:
        file.write(data)
        return True


def custom_input(question: str) -> str:
    """
    Take a question as input from the user and return their response.
    :param question: Question to ask the user
    :return: Users response
    """
    try:
        message = input(question)
        return message
    except (KeyboardInterrupt, EOFError):
        print('\n[x] Script closed.')
        sys.exit()


def main():
    """
    the main function calls it to create the secret key
    :return:
    """
    parser = argparse.ArgumentParser(prog='encrypt data', description='create new encryption key')
    parser.add_argument('filename', type=str, help='name of the secret file to save example my-key.key')
    parser.add_argument('password', type=str, help='Password for key generation')
    args = parser.parse_args()

    file_name = args.filename
    try:
        file_path = create_new_key(args.password, file_name, length=32)
        print(f"A new file was created based on your password. The file name is: {file_path}")
    except (ValueError, FileExistsError) as write_error:
        print(write_error)
        sys.exit(1)


if __name__ == '__main__':
    main()
