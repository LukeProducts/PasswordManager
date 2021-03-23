from Crypto import Random
import Crypto.Cipher.AES as AES
import os
from Crypto.Hash import SHA256
binarys = 32 * 1024
def gather_key(password):
    return SHA256.new(password.encode('utf-8')).digest()
def encrypt(key, filename):
    file_output = "encrypted_passwds/" + "encrypted-" + os.path.basename(filename)
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CFB, IV)
    with open(filename, "rb") as f_in:
        with open(file_output, 'wb') as f_out:
            f_out.write(filesize.encode('utf-8'))
            f_out.write(IV)
            while True:
                binary = f_in.read(binarys)
                if len(binary) == 0:
                    break
                if len(binary) % 16 != 0:
                    binary += b' ' * (16 - (len(binary) % 16))
                f_out.write(encryptor.encrypt(binary))
def decrypt(key, filename):
    file_output = filename.split('-')[1]
    with open(filename, "rb") as f_in:
        filesize = int(f_in.read(16))
        IV = f_in.read(16)
        decryptor = AES.new(key, AES.MODE_CFB, IV)
        with open(file_output, "wb") as f_out:
            while True:
                binary = f_in.read(binarys)
                if len(binary) == 0:
                    break
                f_out.write(decryptor.decrypt(binary))
                f_out.truncate(filesize)