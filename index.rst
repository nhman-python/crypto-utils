Documentation for Encryption Utilities
=====================================

simple2encrypt.py
-------------------

.. module:: simple2encrypt
   :synopsis: Utility functions for encryption and file operations.
   :platform: Unix, Windows

.. versionadded:: 1.5.8

Overview
--------

This module provides utility functions for encryption and file operations.

Module Contents
----------------

.. autosummary::
   :toctree: generated/
   :nosignatures:

   Encryption
   FileIO
   encrypt_walk_dirs
   decrypt_walk_dirs
   custom_input
   main

Classes and Functions
---------------------

.. autoclass:: Encryption
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. autoclass:: FileIO
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: encrypt_walk_dirs
.. autofunction:: decrypt_walk_dirs
.. autofunction:: custom_input
.. autofunction:: main

Installation
------------

To install the Encryption Utilities module, use the following command:

.. code-block:: bash

   pip install simple2encrypt

Usage
-----

Here are some examples of how to use the functions and classes provided by the module:

Encryption Class
~~~~~~~~~~~~~~~~~

You can create an Encryption object to perform encryption and decryption using the AES algorithm.

.. code-block:: python

   from simple2encrypt import Encryption

   key = b'mysecretpassword'
   data = b'sensitive data'

   encryption = Encryption(key, data)
   encrypted_data = encryption.encrypt()
   decrypted_data = encryption.decrypt()

   print("Encrypted data:", encrypted_data)
   print("Decrypted data:", decrypted_data)

FileIO Class
~~~~~~~~~~~~

The FileIO class provides methods for various file operations.

.. code-block:: python

   from simple2encrypt import FileIO

   file_path = '/path/to/file'
   data = b'binary data'

   # Write binary data to a file
   FileIO.write_binary(file_path, data)

   # Read binary data from a file
   read_data = FileIO.read_binary(file_path)

   print("Read data:", read_data)

Encrypting and Decrypting Folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the `encrypt_walk_dirs` and `decrypt_walk_dirs` functions to process files in a folder.

.. code-block:: python

   from simple2encrypt import encrypt_walk_dirs, decrypt_walk_dirs

   folder_path = '/path/to/folder'
   key = b'mysecretpassword'

   # Encrypt files in the folder
   encrypt_walk_dirs(folder_path, key)

   # Decrypt files in the folder
   decrypt_walk_dirs(folder_path, key)

Custom Input
~~~~~~~~~~~~

The `custom_input` function provides a way to take user input with a custom question.

.. code-block:: python

   from simple2encrypt import custom_input

   question = "Enter your name: "
   user_name = custom_input(question)

   print("User name:", user_name)

Generating a Key File
~~~~~~~~~~~~~~~~~~~~~

You can use the `main` function to generate a key file based on a password.

.. code-block:: python

   from simple2encrypt import main

   main()

API Reference
-------------

.. toctree::
   :maxdepth: 2

   simple2encrypt

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
