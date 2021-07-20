import getpass
import base64
import hashlib
from cryptography.fernet import Fernet
# https://github.com/pyca/cryptography
# ferner source code https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py


OUTPUT_MODE = {
    "printEncr": True,
    "printDecr": False,
    "appendFile_encr": "n.txt",
    "appendFile_decr": "b.txt",
}

IO_MESSAGES = {
    "offsetInput": "enter offset(a number): ",
    "taskChoice":"do you want to encrypt (y/n): ",
    "decrFailed": """
        ??????????????????????????????
        ------FAILED TO DECRYPT-------
        (INVALID PASSPHRASE OR OFFSET)
        ??????????????????????????????
    """,
    "encrFailed": """
        ??????????????????????????????
        ------FAILED TO ENCRYPT-------
        (INVALID OFFSET OR SOMETHING)
        ??????????????????????????????
    """,
    "deleteFileWarning": f"""
        ###########################################
        DELETE THIS FILE AFTER YOU USE THE PASSWORD
        ###########################################
    """,
}

def main():
    # either encrypt or decrypt once per call
    key = hashlib.sha256(
        getpass.getpass(prompt="passphrase: ").encode('ascii')
    ).hexdigest()
    offset = int(getpass.getpass(prompt=IO_MESSAGES["offsetInput"])) % 64
    if offset < 32:
        f = Fernet(base64.urlsafe_b64encode(key[offset:offset+32].encode('ascii')))
    else:
        f = Fernet(base64.urlsafe_b64encode(key[offset:offset-32:-1].encode('ascii')))
    del key
    del offset

    while True:
        task = input(IO_MESSAGES["taskChoice"])
        if task == "n":
            break
        # compute cipher_text
        cipher_text = f.encrypt(getpass.getpass(prompt="enter plain_text: ").encode('ascii')).decode()

        if not cipher_text:
            print(IO_MESSAGES["encrFailed"])
        else:
            if OUTPUT_MODE["printEncr"]:
                print(f'genereated token (cipher_text) is \n{cipher_text}')
            if OUTPUT_MODE["appendFile_encr"]:
                comment = input("enter comment/remark for this encrypted content: ")
                with open(OUTPUT_MODE["appendFile_encr"],"a") as fh:
                    fh.writelines([f'\n{comment}: {cipher_text}\n'])
    del f

    # delete all objects in memory
    for obj in dir():
        if not obj.startswith('_'):
            # not all objects are in globals(), so use local() to get them
            if obj in globals():
                del globals()[obj]
            else:
                del locals()[obj]

if __name__ == '__main__':
    main()
