which

searches to directories to find in path 
se un match è trovato sul path, viene risposto





locate 
il modo piu veloce per trovare file sul pc

- sudo updatedb
- locate file.txt


find
sudo find / -name fileé




Find all writable files in /etc:
  $ find /etc -maxdepth 1 -writable -type f
Find all readable files in /etc:
  $ find /etc -maxdepth 1 -readable -type f
Find all directories which can be written to:
$ find / -executable -writable -type d 2> /dev/null