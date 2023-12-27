# Gobuster

Gobuster is a tool used for directory and file brute-forcing in web applications. It helps to discover hidden content, directories, and files on web servers. Gobuster works by sending HTTP requests to a target web server and analyzing the responses to identify valid paths.

## Subdomain

```console
gobuster vhost -w {WORDLIST} -u {TARGET_HOST} --append-domain
```

### Additional Flags
| FLAG | DESCRIPTION | 
| :------------: | :------------: | 
| --exclude-length 334 | To exclude specific length of page, e.g. default error page |


## Directories

```console
gobuster dir --url http://{TARGET_IP}/ --wordlist {WORDLIST}
```

### Additional Flags

| FLAG | DESCRIPTION | 
| :------------: | :------------: | 
| -t | To set the number of threads Gobuster can use |
| -x {extension} | To search only files with the current extension (e.g. php) |