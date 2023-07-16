from encryption_utils import custom_input, Encryption, read_binary


def main():
    """
    The Main function for encrypting and decrypting a message.
    """
    # Get user input
    message = custom_input('Enter your message: ')
    convert = bytes(message.encode())
    try:
        # Read the encryption key from the file
        key = read_binary('my.key')

        # Encrypt the message
        encryptor = Encryption(key, convert)
        encrypted_message = encryptor.encrypt()
        print(f'The encrypted message: {encrypted_message}')

        # Decrypt the message
        decryptor = Encryption(key, encrypted_message)
        decrypted_message = decryptor.decrypt()
        print(f'The decrypted message: {decrypted_message.decode()}')
    except FileNotFoundError:
        print('please run first\npython3 encryption_utils.py file_key your_password')
    except (PermissionError, ValueError) as error:
        print(f'Error: {error}')


if __name__ == '__main__':
    main()
