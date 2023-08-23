import argparse

from simple2encrypt import custom_input, Encryption, FileIO


def main():
    """
    The Main function for encrypting and decrypting a message.
    """
    parser = argparse.ArgumentParser(prog='message encryption',
                                     description='encrypt message with AES encryption from the '
                                                 'key file')
    parser.add_argument('file_key', help='the key to encrypt the message')
    args = parser.parse_args()
    # Get user input
    message = custom_input('Enter your message: ')
    convert = bytes(message.encode())
    try:
        # Read the encryption key from the file
        key = FileIO.read_binary(args.file_key)

        # Encrypt the message
        encryptor = Encryption(key, convert)
        encrypted_message = encryptor.encrypt()
        print(f'The encrypted message: {encrypted_message}')

        # Decrypt the message
        decryptor = Encryption(key, encrypted_message)
        decrypted_message = decryptor.decrypt()
        print(f'The decrypted message: {decrypted_message.decode()}')
    except FileNotFoundError:
        print('please run first\npython3 aes-key file_key your_password')
    except (PermissionError, ValueError) as error:
        print(f'Error: {error}')


if __name__ == '__main__':
    main()
