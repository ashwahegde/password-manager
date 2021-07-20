# How to use

## complete setup
make sure to run `setup.sh` or install dependencies manually.

## Essentials

- think of a big phrase or something, which is easy to remember and hard to predict.  
sha256 of it is used as encryption key
- As of now we are using encryption key of 128 bits for encryption (32 in hexa)  
so `offset` is number used to take required length from sha256 of passphrase (mentioned in previous step).  
so offset given while encryption is necessary while decryption.

## Using python scripts
1. run python script
2. choose to encrypt or decrypt
3. input required things
4. get cipher text or plain text.

```bash
python3 enc-dec.py
```

if you want to encrypt lot at once, use [enc-all_first-time-setup.py](encr-decr/enc-all_first-time-setup.py).

## Configuration

```py
OUTPUT_MODE = {
    "printEncr": True,
    "printDecr": False,
    "appendFile_encr": "out/cipher_text.txt",
    "appendFile_decr": "out/plain_text.txt",
}
```  

1. **printEncr** - print cipher text after encryption is completed.
2. **printDecr** - print plain text after decryption is completed.
3. **appendFile_encr** - append cipher text to this file after encryption is completed.
4. **appendFile_decr** - append plain text to this file after decryption is completed.

set `False` for 1,2 if printing is not needed  
set `None` to 3,4 if appending to file is not required
