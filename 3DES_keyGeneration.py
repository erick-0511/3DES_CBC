from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

key = DES3.adjust_key_parity(get_random_bytes(24))
with open("key3DES.txt", "wb") as keyFile:
    keyb64 = base64.b64encode(key)
    keyFile.write(keyb64)
    print("Key has been saved as 'key3DES.txt'")