# Upload
Like the download process, is very common to upload file inside the target machine, such as linPEAS or winPEAS

## FTP

```console
ftp {TARGET_IP}

put {LOCAL PATH/FILE} {REMOTE PATH}
```

## SSH
Secure Copy Protocol, allows a secure file transfer using SSH.

```console
scp {FILE} {USERNAME}@{TARGET_IP}:{FILE_PATH_TO_WRITE}
```