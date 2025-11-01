from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

keyFile = input("File name with the key: ")
with open(keyFile, "r") as kfile:
    key = base64.b64decode(kfile.read())
    
plaintextFile = input("File with the plaintext: ")
with open(plaintextFile, "rb") as ptFile:
    plaintext = ptFile.read()

iv = get_random_bytes(8)
cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, 8))

with open("IV.txt", "w") as IVfile:
    IVfile.write(base64.b64encode(iv).decode("utf-8"))
    print("\nIV has been saved as 'IV.txt'")

with open("Ciphertext.txt", "w") as cipherFile:
    cipherFile.write(base64.b64encode(ciphertext).decode("utf-8"))
    print("\nCiphertext has been saved as 'Ciphertext.txt'")