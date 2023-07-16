import os
import sys
from encryption_utils import read_binary, write_binary, delete_extension, Encryption


def main():
    try:
        encrypted_file_path = 'newfile.jpg.enc'
        decrypted_file_path = delete_extension(encrypted_file_path)

        # Read the encryption key from the file
        key = read_binary('my-key')

        # Read the encrypted data from file
        encrypted_data = read_binary(encrypted_file_path)

        # Decrypt the data
        decryption_obj = Encryption(key, encrypted_data)
        decrypted_data = decryption_obj.decrypt()

        # Write the decrypted data to a new file
        write_binary(decrypted_file_path, decrypted_data)

        # Remove the encrypted file
        os.remove(encrypted_file_path)
    except (FileNotFoundError, ValueError, PermissionError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
