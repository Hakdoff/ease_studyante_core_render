# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes


# pad with spaces at the end of the text
# beacuse AES needs 16 byte blocks
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '

# remove the extra spaces at the end


def unpad(s):
    return s.rstrip()


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(
        bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


# def main():
#     password = "SECRET_KEY"
#     student = "JR2"
#     # First let us encrypt secret message

#     # FOR ENCRYPTION
#     encrypted = encrypt("15434d93-6ed0-42e1-9451-26f1ba5cfedc", password)
#     print(encrypted)

#     # TO BE SAVE IN DJANGO QR_CODE
#     aes_256 = f'{encrypted["cipher_text"]}${encrypted["salt"]}${encrypted["nonce"]}${encrypted["tag"]}'
#     print(aes_256)
#     # FOR DECRYPTION
#     aes_256_split = aes_256.split('$')

#     print(aes_256_split)

#     temp_encrpyted = {
#         'cipher_text': aes_256_split[0],
#         'salt': aes_256_split[1],
#         'nonce': aes_256_split[2],
#         'tag': aes_256_split[3]
#     }

#     print(temp_encrpyted)

#     # Let us decrypt using our original password
#     decrypted = decrypt(temp_encrpyted, password)
#     student = bytes.decode(decrypted)
#     print(student)


# main()
