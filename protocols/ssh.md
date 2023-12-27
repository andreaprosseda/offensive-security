# SSH

Secure Shell, cryptographic network protocol used for secure communication over an unsecured network. It is commonly used to access and manage remote servers securely. SSH provides a secure channel for data exchange between two devices, typically a client and a server.

```console
ssh {USERNAME}@{TARGET_IP}
```

# Create Authorized Key
1. Create a ssh key pair with command `ssh-keygen` 
2. Copy `public_key.pub` in /root/.ssh/authorized_keys
3. Try to login with private key

```console
ssh -i private_key root@{TARGET_IP}
```

# Tips
* Try writing own SSH public key in `/root/.ssh/authorized_keys`