from setuptools import setup
description = """
encryption-utils
================

encryption-utils is a Python library that provides utility functions for encryption and file operations. It leverages 
the AES (Advanced Encryption Standard) algorithm for secure encryption and decryption of data.

Features
--------
- Encryption and decryption using the AES algorithm in CBC (Cipher Block Chaining) mode.
- Password-based key generation using PBKDF2 (Password-Based Key Derivation Function 2).
- File operations for reading and writing binary data.
- Utility functions for removing file extensions and taking user input.
- Command-line interface for creating a new encryption key based on a password.

Installation
------------
You can install `encryption-utils` using pip:

shell
pip install encryption-utils


Usage
-----
Here's a simple example demonstrating how to use `encryption-utils` to encrypt data:

from encryption_utils import Encryption

# Create an instance of Encryption with a key and data
key = generate_key('your_key', 32)  # Replace with your own key
data = b'some_data_to_encrypt'  # Replace with the data you want to encrypt
encryption = Encryption(key, data)

# Encrypt the data
encrypted_data = encryption.encrypt()
print('Encrypted data:', encrypted_data)

Please note that `encryption-utils` requires the `pycryptodome` package as a dependency. It is recommended to have it installed before using the library.

For more details and usage examples, refer to the documentation.

Contributing
------------
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository: [link-to-repo](https://github.com/nhman-python/crypto-utils).

License
-------
This project is licensed under the MIT License. See the LICENSE file for more information.
"""


setup(
    name='my-encryption-utils',
    version='1.1',
    description='Utility functions for encryption and file operations',
    author='nhman python',
    author_email='wbgblfix@duck.com',
    long_description=description,
    py_modules=['encryption_utils'],
    install_requires=[
        'pycryptodome',  # Dependency on pycryptodome package
    ],
)
