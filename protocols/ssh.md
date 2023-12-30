# SSH

Secure Shell, cryptographic network protocol used for secure communication over an unsecured network. It is commonly used to access and manage remote servers securely. SSH provides a secure channel for data exchange between two devices, typically a client and a server.

```console
# if password is known
ssh {USERNAME}@{TARGET_IP}

# if private key (id_rsa) is known
ssh -i private_key root@{TARGET_IP}
```

## Create Authorized Key
1. Create a ssh key pair with command `ssh-keygen` 
2. Copy `id_rsa.pub` in /root/.ssh/authorized_keys
3. Try to login with private key `id_rsa`

## Keys from .ppk
PuTTY is one of the most common SSH Client. It has its own key format, that is `ppk`.
A ppk file has this format

```console
PuTTY-User-Key-File-3: ssh-rsa
Encryption: [...]
Comment: [...]
Public-Lines: [...]
[...]
Private-Lines: [...]
[...]
Private-MAC: [...]
```

We can retrieve public and private keys using this commands:
```console
# Public Key
puttygen {PUTTY_FILE}.ppk -O public-openssh -o id_rsa.pub

# Private Key
puttygen {PUTTY_FILE}.ppk -O private-openssh -o id_rsa

chmod 600 id_rsa
```


## Tips
* Try writing own SSH public key in `/root/.ssh/authorized_keys`
* Try to gain a private key and use it to connect