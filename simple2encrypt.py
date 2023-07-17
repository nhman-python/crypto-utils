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

__version__ = '1.5.4'


class Encryption:
    """
    A class for performing encryption and decryption using the AES algorithm.
    """

    def __init__(self, key: bytes, data: bytes):
        """
        Initialize the Encryption object with the key and data.
        :param key: Encryption key
        :param data: Data to be encrypted or decrypted
        """
        self.key = key
        self.data = data

    def encrypt(self) -> bytes:
        """
        Encrypt the data using the AES algorithm.
        :return: Encrypted data
        """
        cipher = AES.new(self.key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(pad(self.data, cipher.block_size))
        return cipher.iv + encrypted_data

    def decrypt(self) -> bytes:
        """
        Decrypt the data using the AES algorithm.
        :return: Decrypted data
        """
        initialization_vector = self.data[:AES.block_size]  # Extract the IV from the data
        cipher = AES.new(self.key, AES.MODE_CBC, iv=initialization_vector)
        decrypted_data = cipher.decrypt(self.data[AES.block_size:])
        return unpad(decrypted_data, cipher.block_size)


def folder_encrypt(folder_path: str, key: bytes, add_extension='.enc') -> None:
    """
    Encrypts all files within a given folder.

    :param add_extension: Add the extension to the end of the file
    :param folder_path: Path to the folder containing the files to be encrypted.
    :param key: The key for encryption.
    :raises ValueError: If the provided folder path is not a directory.
    """
    if not os.path.isdir(folder_path):
        raise ValueError("Expected a folder path, but received a different type of path.")

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            data = read_binary(full_path)
            encryption = Encryption(key, data)
            encrypted_data = encryption.encrypt()
            new_file_path = full_path + add_extension
            write_binary(new_file_path, encrypted_data)
            os.remove(full_path)


def folder_dencrypt(folder_path: str, key: bytes) -> None:
    """
    Decrypts all files within a given folder.

    :param folder_path: Path to the folder containing the files to be decrypted.
    :param key: The key for decryption.
    :raises ValueError: If the provided folder path is not a directory.
    """
    if not os.path.isdir(folder_path):
        raise ValueError("Expected a folder path, but received a different type of path.")

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            data = read_binary(full_path)
            decryption = Encryption(key, data)
            decrypted_data = decryption.decrypt()
            new_file_path = delete_extension(full_path)
            write_binary(new_file_path, decrypted_data)
            os.remove(full_path)


def delete_extension(path: str) -> str:
    """
    Remove the last file extension from a path.

    :param path: The file path
    :return: The path without the last extension
    """
    dir_name, basename = os.path.split(path)
    while '.' in basename:
        basename, extension = os.path.splitext(basename)
        if extension:
            return os.path.join(dir_name, basename)
    return path


def generate_key(password: str, length: int) -> bytes:
    """
    Create a new key based on the password and save it to a file.
    :param password: Password for a key generation
    :param length: Length key
    :return: the new key
    """
    valid_lengths = [16, 24, 32]
    if length not in valid_lengths:
        raise ValueError('Invalid key length. Choose length from this list: [16, 24, 32]')
    salt = os.urandom(length)
    key = PBKDF2(password, salt, dkLen=32)
    return key


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
    with open(file_path, 'rb') as f:
        return f.read()


def write_binary(file_path, data) -> bool:
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
    with open(file_path, 'wb') as f:
        f.write(data)
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
    password = args.password
    file_name = args.filename
    try:
        key = generate_key(password, length=32)
        write_binary(file_name, key)
        print(f"A new file was created based on your password. The file name is: {file_name}")
    except (ValueError, FileExistsError, FileNotFoundError) as write_error:
        print(write_error)
        sys.exit()


if __name__ == '__main__':
    main()
