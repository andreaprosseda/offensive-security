# FTP

File Transfer Protocol, standard protocol used to transfer files from one host to another over a TCP-based network (often used for uploading and downloading files to and from a server)

```console
ftp {TARGET_IP}

# force active mode
ftp -A {TARGET_IP}
```

* *Default Port*: 21

## Anonymous
FTP could allow anonymous access. It usually accepts any string as password, but it is common to use or a password like:
* anonymous
* guest
* email (anonymous@domain.com)

## Bruteforce

We can try to use bruteforce to guess the FTP password using hydra
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_IP} -t 4 ftp
```

## Commands

| COMMAND | DESCRIPTION | 
| :------------: | :------------: | 
| ? | To request the list of supported commands |
| dir | To display the content of the current REMOTE directory |
| lcd | To display the current LOCAL directory |
| cd {dir_path} | To change the current REMOTE directory |
| lcd {dir_path} | To change the current LOCAL directory |
| get {file_path} [dir] | To download a file to the current LOCAL directory [or specific directory] |
| put {file_path} [dir] | To upload a file to the current REMOTE directory [or specific directory] |
| get {path_regex} [dir] | To download a list of files (es *.txt) to the current LOCAL directory [or specific directory] |
| put {path_regex} [dir] | To upload a list of files (es *.txt) to the current REMOTE directory [or specific directory] |
| exit | To terminate the FTP connection |

# Tips
* Check for anonymous authentication
* Use common_pass.txt or rockyou.txt as wordlist for bruteforce