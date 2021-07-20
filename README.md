# password-manager

useful for storing encrypted passwords in a file and sync to a cloud storage.

## Motivation
As we use lot of applications and services which requires password authentication, remembering every password is not possible. (using same password for for all is not at all recommended)

General problems are:
- Many people write down passwords on paper(notebook).
    - if the book is lost: everything is lost.
    - if the book is found by others: passwords can be used by someone,
    very dangerous financially or any other means.
    - you cannot keep it always with you.

- Some people keep copy of all passwords in a file (say excel sheet).
    - if it is not encrypted: you are vulnerable to above issues.
    - if it is encrypted: when file is decrypted on a compromised machine all
    passwords can be obtained by the malware.

### I had tried a way 😂
- I was using some simple(secret) rules to modify and store cipher texts in a book.
my friends were unable to read it. But I am pretty sure if it is given to computer(may be simple NLP model) with few known(plain/actual) texts, whole pattern can be found out in few minutes.  
- other problems were:
    - remembering pattern/rules
    - computing cipher text in the mind
    - was confused with the complicated rules created by myself 😆


## Goal of the solution

- Encrypt individual passwords individually.
- Encryption and decryption keys are generated at runtime.
- sha256 of master password (passphrase) is used to encrypt all passwords.
- enforce maximum security in python script.

## Setup
It can be used with any operating system.  
The [setup script](setup.sh) will work in linux and mac.

## Usage
refer [this file](encr-decr/USAGE.md).

## Feedback
- create an issue.
- ping me on [telegram](https://t.me/ashwahegde).
