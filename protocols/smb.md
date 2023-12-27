# SMB

Service Message Block, communication protocol used to provide shared access to files, printers, and serial ports between endpoints on a network. 

```console
smbclient \\\\{TARGET_IP}\\{USERNAME}
```

* *Default Ports*: 139, 445

## Anonymous
SMB could allow anonymous access. We can use our local username and a blank password or `-N` that specifies no password

```console
smbclient -N -L {TARGET_ID}
```

This command will list available shared resources

## Commands

| COMMAND | DESCRIPTION | 
| :------------: | :------------: | 
| ? / help | To request the list of supported commands |
| dir | To display the content of the current REMOTE directory |
| lcd | To display the current LOCAL directory |
| cd {dir_path} | To change the current REMOTE directory |
| lcd {dir_path} | To change the current LOCAL directory |
| get {file_path} [dir] | To download a file to the current LOCAL directory [or specific directory] |
| put {file_path} [dir] | To upload a file to the current REMOTE directory [or specific directory] |
| get {path_regex} [dir] | To download a list of files (es *.txt) to the current LOCAL directory [or specific directory] |
| put {path_regex} [dir] | To upload a list of files (es *.txt) to the current REMOTE directory [or specific directory] |