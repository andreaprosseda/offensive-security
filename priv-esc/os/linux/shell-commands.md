# Useful Shell Commmands
Here a list of useful commands in Linux

## Grep

```console
grep -Rni PATH file

grep -Rni PATH -e '$SHA$'
```

### Common Flags
| FLAG | DESCRIPTION | 
| :------------: | :------------: | 
| -R | Recursive following all symlinks |
| -n | Print line number |
| -i | Ignore case |
| -w | Match whole words only |
| -e 'REG_PATTERN'| 
| --binary-files=text | Treat binary files as text files |
| --exclude-dir={dir1,dir2,*.dst} | Exclude directories from the search | 


Grep output can be manipulated to remove the prefix with sed, then can be sort:

```console
grep -Rni '/var/www/site' -e '{SHA}' | sed 's/.*{SHA}//' | sort -u
```


## Find

cerca file con estensione .key, i file non leggibili (permission denied, vengono rediretti su dev/null)
find /percorso/della/cartella -type f -name "*.key" -readable 2>/dev/null


sudo find / -name file

Find all writable files in /etc:
  $ find /etc -maxdepth 1 -writable -type f
Find all readable files in /etc:
  $ find /etc -maxdepth 1 -readable -type f
Find all directories which can be written to:
#$ find / -executable -writable -type d 2> /dev/null

## Locate

locate 
il modo piu veloce per trovare file sul pc

- sudo updatedb
- locate file.txt

