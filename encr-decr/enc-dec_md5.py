import getpass
import base64
import hashlib
from cryptography.fernet import Fernet

try:
    key = base64.urlsafe_b64encode(
        hashlib.md5(
            getpass.getpass().encode('ascii')
        ).hexdigest().encode('ascii')
    )
    f = Fernet(key)
    del key
    if input("do you want to encrypt (y/n): ") == "y":
        cipher_text = f.encrypt(getpass.getpass(prompt="enter plain_text: ").encode('ascii')).decode()
        print(f'genereated token (cipher_text) is \n{cipher_text}')
        del cipher_text
    else:
        plain_text = f.decrypt(getpass.getpass(prompt="enter cipher_text: ").encode('ascii')).decode()
        print(f'decrypted plain_text is: \n{plain_text}')
        del plain_text
    del f
    print("completed")
except Exception as e:
    print(e)
    for obj in dir():
        if not obj.startswith('_'):
            del globals()[obj]
