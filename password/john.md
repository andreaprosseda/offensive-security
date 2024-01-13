# John the Ripper
John the Ripper is a command-line tool used for password cracking softwares.

```console
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

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