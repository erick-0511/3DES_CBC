from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

keyFile = input("File name with the key: ")
with open(keyFile, "r") as kfile:
    key = base64.b64decode(kfile.read())
    
ivFile = input("File with the IV: ")
with open(ivFile, "r") as iFile:
    iv = base64.b64decode(iFile.read())
    
ciphertextFile = input("File with the ciphertext: ")
with open(ciphertextFile, "r") as ctFile:
    ciphertext = base64.b64decode(ctFile.read())
    
decipher = DES3.new(key, DES3.MODE_CBC, iv)
plaintext = unpad(decipher.decrypt(ciphertext), 8)

with open("Plaintext.txt", "wb") as ptFile:
    ptFile.write(plaintext)
    print("\nPlaintext has been saved as 'Plaintext.txt'")