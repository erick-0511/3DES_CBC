# 3DES MODE CBC

## Description
Python programam that implements 3DES in CBC mode using the pycryptodome library. The implementation is divided into 3 parts:
- Key generation 
- Encrypt and save
- Decrypt and save
Note: Base64 is used

## Characteristics
3DES_KeyGeneration:
- The program generates a random key and saves it to a text file

3DESCBC:
- Read the key file
- Read the plaintext file (any extension)
- Generates and saves IV to a text file
- Encrypt the plaintext and saves it to a text file

3DESCBCDecipher:
- Read the key file
- Read the IV file
- Read the ciphertext file file
- Decrypt the ciphertext and saves it to a text file

## Installation and execution
To install the library, use:

<div aling="center">pip install prycryptodome</div>


To execute the program:

<div aling="center">py 3DES_KeyGeneration.py</div>
<div aling="center">py 3DESCBC.py</div>
<div aling="center">py 3DESCBCDecipher.py</div>