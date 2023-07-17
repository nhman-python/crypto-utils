Documentation for Encryption Utilities
=====================================

encryption_utils.py
-------------------

.. automodule:: encryption_utils
   :members:
   :undoc-members:
   :show-inheritance:

Overview
--------

This module provides utility functions for encryption and file operations.

Installation
------------

To install the Encryption Utilities module, use the following command:

.. code-block:: bash

   pip install encryption-utils

Usage
-----

Here are some examples of how to use the functions provided by the module:

Encrypting a Folder
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import folder_encrypt

   folder_path = '/path/to/folder'
   key = b'mysecretpassword'

   folder_encrypt(folder_path, key)

   print("Folder encryption completed.")

Decrypting a Folder
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import folder_decrypt

   folder_path = '/path/to/folder'
   key = b'mysecretpassword'

   folder_decrypt(folder_path, key)

   print("Folder decryption completed.")

Generating a Key
~~~~~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import generate_key

   password = 'mysecretpassword'
   key = generate_key(password, length=32)

   print("Generated key:", key)

Writing Binary Data to a File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import write_binary

   file_path = '/path/to/file'
   data = b'binary data'

   write_binary(file_path, data)

Reading Binary Data from a File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import read_binary

   file_path = '/path/to/file'

   data = read_binary(file_path)

Custom Input
~~~~~~~~~~~~

.. code-block:: python

   from encryption_utils import custom_input

   question = "Enter your name: "
   user_name = custom_input(question)

   print("User name:", user_name)

API Reference
-------------

.. toctree::
   :maxdepth: 2

   simple2encript

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
