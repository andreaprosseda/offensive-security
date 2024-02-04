# John the Ripper
John the Ripper is a command-line tool used for password cracking softwares.

```console
john --wordlist=/usr/share/wordlists/rockyou.txt hash
```

## Format Specific Cracking
Sometimes John cannot recognize automatically the hash type provided, so we need to provide a specific format.
We can identify the hash using Hash Identifier

```console
hash-identifier {HASH}
```

Then we can use it as FORMAT parameter

```console
john --wordlist=/usr/share/wordlists/rockyou.txt hash --format={FORMAT}
```

We can list and search the format needed with the following command
```console
john --list=formats | grep -iF "md5"
```

N.B. john requires the prefix `raw-` in order to recognize standard hashtypes 


## Common Utilities
John offers a huge amount of utilities able to export the hash to crack

```console
ssh2john id_rsa > hash.txt
```

Here a list of the most common utilities:
| UTILITY | FILE EXTENSION |
| :-----: | :------------: |
| 1password2john | .1password / .1pif |
| keychain2john | .keychain |
| keepass2john | .kdbx / .kdb |
| openssl2john | .crt / .cer / .key |
| pem2john | .pem |
| putty2john | .ppk |
| rar2john | .rar |
| ssh2john | .pub | 
| zip2john | .zip |


## Unshadowing
John offers the possibility to crack Windows (using --format=NT) and Linux password. On Linux OS, we can use the unshadow utility in order to obtain an input for John

```console
unshadow etc_passwd etc_shadow > hash

john --wordlist=/usr/share/wordlists/rockyou.txt hash --format=sha512crypt
```

## Single - Word Mangling
Suppose to know the hash contains a password similar to Joker (es Jok3r).

```console
# Create a file containing word:hash
echo "Joker:7bf6d9bb82bed1302f331fc6b816aada" > hash

john --single hash --format=raw-md5
```