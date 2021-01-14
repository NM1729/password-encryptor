#Fernet is a symmetric key cryptography implementation
#It ensures that the cipher cannot be decrypted without the key

import cryptography
from cryptography.fernet import Fernet
key = b'HIUez0N9nmjwaQ2CZLbFUaGro9EczOqgaYSun7mgTGo='

cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"Texttobeencrypted123")
print(ciphered_text)