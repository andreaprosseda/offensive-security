# DirSearch
DirSearch is advanced web path brute-forcer

```console
dirsearch -u {TARGET_URL}

dirsearch -u {TARGET_URL} -w {WORDLIST} -t {THREADS}

```

## Additional Flags
| FLAG | DESCRIPTION | 
| :------------: | :------------: | 
| -r | Brute-force resursively |
| -e {extensions} | Retrie only these extensions separated by commas (e.g. php,asp) |
| -t {threads} | Number of threads to use | 
| --min-response-size=LENGTH | Minimum response length to include |
| --max-response-size=LENGTH | Maximum response length to include |

## Exclusions

```console
# Exclude status codes, separated by commas, support ranges (e.g. 301,500-599)
dirsearch -e php,html,js -u {TARGET_URL} -x 301,500-599

# Exclude responses by sizes, separated by commas (e.g. 0B,4KB)
dirsearch -e php,html,js -u {TARGET_URL} --exclude-sizes 1B,243KB

# Exclude responses by text, can use multiple flags
dirsearch -e php,html,js -u {TARGET_URL} --exclude-texts "403 Forbidden"

# Exclude responses by regular expression
dirsearch -e php,html,js -u {TARGET_URL} --exclude-regexps "^Error$"

# Exclude responses if this regex (or text) matches redirect URL (e.g. '/index.html')
dirsearch -e php,html,js -u {TARGET_URL} --exclude-redirects "https://(.*).okta.com/*"

# Exclude responses similar to response of this page, path as input (e.g. 404.html)
dirsearch -e php,html,js -u {TARGET_URL} --exclude-response /error.html

# If there are sub-directories that you do not want to brute-force recursively
dirsearch -e php,html,js -u {TARGET_URL} -r --exclude-subdirs image/,media/,css/
```


## Intercept with Proxy
DirSearch requests can be inspected using Burp, in order to understand what is wrong about the request.
DirSearch needs just the setup of the following environment variable

```console
dirsearch -e php,html,js -u {TARGET_URL} --proxy 127.0.0.1:8080
```
