from setuptools import setup

description = """
# simple2encrypt

`simple2encrypt` is a Python library that provides utility functions for encryption and file operations. It 
includes functionalities for encrypting and decrypting data using the AES algorithm, generating encryption keys, 
reading and writing binary data from/to files, handling user input, and encrypting/decrypting individual files.

## Installation

You can install `simple2encrypt` using `pip`:

```
pip install simple2encrypt
```

## Usage

### Encryption

To perform encryption and decryption using the AES algorithm, you can use the `Encryption` class provided by the library. Here's an example:

```
from simple2encrypt import Encryption

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

### File Operations

The `FileIO` class provides functions for reading and writing binary data to files, as well as deleting file extensions. Here's an example:

```
from simple2encrypt import FileIO

file_path = 'myfile.txt'
data_to_write = b'mydata'

# Read binary data from a file
read_data = FileIO.read_binary(file_path)
print("Read data:", read_data)

# Write binary data to a file
FileIO.write_binary(file_path, data_to_write)
print("Data written to file successfully.")

# Remove file extension
file_name_without_extension = FileIO.delete_extension(file_path)
print("File name without extension:", file_name_without_extension)
```

### Folder Encryption

The `WalkDirs` class allows you to encrypt and decrypt all files within a specified folder using a given key. Here's an example:

```
from simple2encrypt import WalkDirs

folder_path = '/path/to/folder'
key = b'mysecretpassword'
folder_encryptor = WalkDirs(folder_path, key)

# Encrypt all files in the folder
folder_encryptor.encrypt()

# Decrypt all files in the folder
folder_encryptor.decrypt()
```

### Encrypting/Decrypting Individual Files

The `EncryptFile` class provides a way to encrypt and decrypt individual files. Here's an example:

```
from simple2encrypt import EncryptFile

file_path = 'file.txt'
key = b'mysecretpassword'
data_to_encrypt = b'mydata'

# Encrypt the file
file_encryptor = EncryptFile(file_path, key, data_to_encrypt)
file_encryptor.encrypt()

# Decrypt the file
file_decryptor = EncryptFile(file_path + '.enc', key)
file_decryptor.decrypt()
```

### Handling User Input

The `custom_input` function allows you to prompt the user for input and retrieve their response. Here's an example:

```
from simple2encrypt import custom_input

question = "Enter your name: "
user_name = custom_input(question)
print("User name:", user_name)
```

### Creating Encryption Key (Command Line)

The library also provides a command-line interface for creating a new encryption key. Here's an example usage:

```
aes-key [file name] [secret-password]
```

This will create a new encryption key file named `key.bin` based on the provided password.

## Version

The current version of `simple2encrypt` is 1.6.6

## License

This library is distributed under the [MIT License](https://github.com/nhman-python/crypto-utils/blob/main/LICENSE). 
See the `LICENSE` file for more information.
```
"""

setup(
    name='simple2encrypt',
    version='1.6.6',
    description='Utility functions for encryption and file operations',
    author='nhman-python',
    author_email='wbgblfix@duck.com',
    url='https://github.com/nhman-python/crypto-utils',
    license='MIT',
    long_description=description,
    long_description_content_type='text/markdown',
    py_modules=['simple2encrypt', 'example_message', 'example_encrypt', 'example_decrypt'],
    install_requires=[
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': ['aes-key = simple2encrypt:main', 'aes-message = example_message:main',
                            'aes-encrypt = example_encrypt:main', 'aes-decrypt = example_decrypt:main'],
    },
)
