# KeePass
KeePass is an open-source password manager that allows users to store and manage their passwords

# 2.X Dumper

https://github.com/vdohney/keepass-password-dumper?tab=readme-ov-file

# Bruteforce
```console
# Export hash to a file
keepass2john {DB_NAME}.kdbx > keepass.hash

# Try cracking with a wordlist
john --wordlist={WORDLIST} keepass.hash
```

# Tips
* If you have a partial password, google it instead of (before) bruteforce only few chars
* Use rockyou.txt as wordlist