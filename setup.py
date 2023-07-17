from setuptools import setup

description = """
# Encryption Utils

`encryption_utils` is a Python library that provides utility functions for encryption and file operations. It 
includes functionalities for encrypting and decrypting data using the AES algorithm, generating encryption keys, 
reading and writing binary data from/to files, and handling user input.

## Installation

You can install `encryption_utils` using `pip`:

```
pip install simple2encrypt
```

## Usage
simple2encrypt
### Encryption

folder_encrypt
--------------

.. py:function:: folder_encrypt(folder_path: str, key: bytes, add_extension: str = '.enc') -> None

   Encrypts all files within a given folder.

   :param folder_path: Path to the folder containing the files to be encrypted.
   :type folder_path: str
   :param key: The key for encryption.
   :type key: bytes
   :param add_extension: Add the extension to the end of the file (default: '.enc')
   :type add_extension: str, optional
   :raises ValueError: If the provided folder path is not a directory.
   :returns: None

folder_decrypt
--------------

.. py:function:: folder_decrypt(folder_path: str, key: bytes) -> None

   Decrypts all files within a given folder.

   :param folder_path: Path to the folder containing the files to be decrypted.
   :type folder_path: str
   :param key: The key for decryption.
   :type key: bytes
   :raises ValueError: If the provided folder path is not a directory.
   :returns: None


To perform encryption and decryption using the AES algorithm, you can use the `Encryption` class provided by the 
library. Here's an example:

```
from encryption_utils import Encryption

# Initialize the Encryption object with the key and data
key = b'mysecretpassword'  # Encryption key
data = b'mydata'  # Data to be encrypted or decrypted
encryption = Encryption(key, data)

# Encrypt the data
encrypted_data = encryption.encrypt()
print("Encrypted data:", encrypted_data)

# Decrypt the data
decrypted_data = encryption.decrypt()
print("Decrypted data:", decrypted_data)
```

### Removing File Extension

The `delete_extension` function can be used to remove the file extension from a path. Here's an example:

```
from encryption_utils import delete_extension

file_path = 'file.txt.enc'
file_name = delete_extension(file_path)
print("File name without extension:", file_name)
```

### Generating Encryption Keys

The `generate_key` function allows you to generate a new key based on a password. Here's an example:

```
from encryption_utils import generate_key

password = 'mysecretpassword'  # Password for key generation
length = 32  # Key length (choose from [16, 24, 32])
key = generate_key(password, length)
path_key = 'key.bin'
print("Generated key:", key)
write_binary(path_key, key)

```

### Reading and Writing Binary Data

The `read_binary` and `write_binary` functions can be used to read and write binary data from/to files, respectively. 
Here's an example:

```
from encryption_utils import read_binary, write_binary

file_path = 'file.bin'

# Read binary data from a file
data = read_binary(file_path)
print("Read data:", data)

# Write binary data to a file
data_to_write = b'mydata'
write_binary(file_path, data_to_write)
print("Data written to file successfully.")
```

### Handling User Input

The `custom_input` function allows you to prompt the user for input and retrieve their response. Here's an example:

```
from encryption_utils import custom_input

question = "Enter your name: "
user_name = custom_input(question)
print("User name:", user_name)
```

### Creating Encryption Key (Command Line)

The library also provides a command-line interface for creating a new encryption key. Here's an example usage:

aes-key  # Executes the main function from encryption_utils module
```
aes-key [file name] [secret-password]
```
aes-message  # Executes the main function from example_message module


This will create a new encryption key file named `my-key.bin` based on the provided password.

## Version

The current version of `encryption_utils` is 1.5.3

## License

This library is distributed under the [MIT License](https://github.com/nhman-python/crypto-utils/blob/main/LICENSE). 
See the `LICENSE` file for more information.

"""

setup(
    name='simple2encrypt',
    version='1.5.3',
    description='Utility functions for encryption and file operations',
    author='nhman-python',
    author_email='wbgblfix@duck.com',
    url='https://github.com/nhman-python/crypto-utils',
    license='MIT',
    long_description=description,
    long_description_content_type='text/markdown',
    py_modules=['encryption_utils', 'example_message'],
    install_requires=[
        'pycryptodome',  # Dependency on pycryptodome package
    ],
    entry_points={
        'console_scripts': ['aes-key = encryption_utils:main', 'aes-message = example_message:main', ],
    },
)
