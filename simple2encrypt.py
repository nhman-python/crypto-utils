"""
encryption_utils.py
Utility functions for encryption and file operations.
"""

import os
import sys
import argparse
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

__version__ = '1.6.6'


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

    def _get_cipher(self, iv: bytes = None) -> AES:
        return AES.new(self.key, AES.MODE_CBC, iv=iv)

    def encrypt(self) -> bytes:
        """
        Encrypt the data using the AES algorithm.
        :return: Encrypted data
        """
        cipher = self._get_cipher()
        encrypted_data = cipher.encrypt(pad(self.data, cipher.block_size))
        return cipher.iv + encrypted_data

    def decrypt(self) -> bytes:
        """
        Decrypt the data using the AES algorithm.
        :return: Decrypted data
        """
        initialization_vector = self.data[:AES.block_size]
        cipher = self._get_cipher(iv=initialization_vector)
        decrypted_data = cipher.decrypt(self.data[AES.block_size:])
        return unpad(decrypted_data, cipher.block_size)


class FileIO:
    """
    A class for performing file operations.
    """
    VALID_KEY_LENGTHS = {16, 24, 32}

    @staticmethod
    def generate_key(password: str, length: int) -> bytes:
        """
        Create a new key based on the password and save it to a file.
        :param password: Password for key generation
        :param length: Length of the key
        :return: The new key
        """
        if length not in FileIO.VALID_KEY_LENGTHS:
            raise ValueError(f"Invalid key length. Choose length from this list: {FileIO.VALID_KEY_LENGTHS}")
        salt = os.urandom(length)
        key = PBKDF2(password, salt, dkLen=32)
        return key

    @staticmethod
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

    @staticmethod
    def write_binary(file_path: str, data: bytes) -> None:
        """
        Write binary data to a file.
        :param file_path: Path of the file to write the data to
        :param data: Data to write
        """
        with open(file_path, 'wb') as f:
            f.write(data)

    @staticmethod
    def delete_extension(path: str) -> str:
        """
        Remove the last file extension from a path.
        """
        root, ext = os.path.splitext(path)
        return root


class WalkDirs:
    def __init__(self, folder_path: str, key: bytes):
        self.folder_path = folder_path
        self.key = key

    def encrypt(self, extension: str = '.enc') -> None:
        """
        Walks through the specified folder path and encrypts all files using the provided AES key.
        """
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    data = FileIO.read_binary(file_path)
                    encrypted_data = Encryption(self.key, data).encrypt()
                    os.remove(file_path)
                    new_file = f'{file_path}{extension}'
                    FileIO.write_binary(new_file, encrypted_data)
                except (PermissionError, FileExistsError, FileNotFoundError, ValueError) as err:
                    raise err

    def decrypt(self, output=None) -> None:
        """
        Walks through the specified folder path and decrypts all files using the provided AES key.
        """
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    data = FileIO.read_binary(file_path)
                    decrypted_data = Encryption(self.key, data).decrypt()
                    if output:
                        FileIO.write_binary(output, decrypted_data)
                    else:
                        new_path = FileIO.delete_extension(file_path)
                        FileIO.write_binary(new_path, decrypted_data)
                    os.remove(file_path)
                except (PermissionError, FileExistsError, FileNotFoundError, ValueError) as err:
                    raise err


class EncryptFile:
    def __init__(self, file_path: str, key: bytes, data: bytes, extension='.enc'):
        self.key = key
        self.data = data
        self.file_path = file_path
        self.extension = extension

    def encrypt(self):
        enc_data = Encryption(self.key, self.data).encrypt()
        new_path = self.file_path + self.extension
        FileIO.write_binary(new_path, enc_data)
        os.remove(self.file_path)

    def decrypt(self, output=None):
        try:
            enc_data = FileIO.read_binary(self.file_path)
            dec_data = Encryption(self.key, enc_data).decrypt()
            if output:
                FileIO.write_binary(output, dec_data)
            else:
                new_path = FileIO.delete_extension(self.file_path)
                FileIO.write_binary(new_path, dec_data)
            os.remove(self.file_path)
        except ValueError:
            print('Wrong key!')


def custom_input(question: str) -> str:
    """
    Take a question as input from the user and return their response.
    """
    try:
        message = input(question)
        return message
    except (KeyboardInterrupt, EOFError):
        print('\n[x] Script closed.')
        sys.exit()


def main():
    """
    The main function to create the secret key.
    """
    parser = argparse.ArgumentParser(prog='encrypt data', description='create new encryption key')
    parser.add_argument('filename', type=str, help='name of the secret file to save, e.g., my-key.key')
    parser.add_argument('password', type=str, help='Password for key generation')
    args = parser.parse_args()
    password = args.password
    file_name = args.filename
    try:
        key = FileIO.generate_key(password, length=32)
        FileIO.write_binary(file_name, key)
        print(f"A new file was created based on your password. The file name is: {file_name}")
    except (ValueError, FileExistsError, FileNotFoundError) as write_error:
        print(write_error)
        sys.exit()


if __name__ == '__main__':
    main()
