#Nmap

```console
nmap 192.168.1.1

nmap -sT -sU 192.168.1.1

sudo nmap -Pn -p- -A --min-rate 5000 -oN scan.txt {TARGET_IP}

```

[!WARNING]
nmap default port scanning will scan only the 1000 most popular ports

| OPTIONS | DESCRIPTION | NOTE |
| :------------: | :------------: | ------------ |
| -sS | TCP scan [Stealth Mode] | It doesn't complete handshake with ACK. Older firewalls didn't log for uncomplete handshakes, but now is misleading |
| -sT | TCP scan [Connect Mode] | Completes the handshake. It is heavier than -sS because is 3-way |
| -sU | UDP scan | Uses standard methods (empty packets) + Protocol-Specific (like SMTP) |
| -sn | Ping scan | Uses to ping the host, used for Network Sweeping |
| -sV | Service scan | Uses to understand the service that is running on current port |
| -oG | Save Output [Greppable Mode] | Save the output in a file given a filepath | 
| -A | Advanced Information | Detect OS, version, scripts and traceroute |
| -O | OS Fingerprinting | Guess the target's OS inspecting returned packets |







N.B.
Da valutare creazione di script per nmap


lite
sudo nmap -sC -sV -oA broker IP

full
sudo nmap -p- --min-rate=5000 -oG broker-all ip

prendiamo tutte le porte aperte, poi
sudo nmap -sC -sV -oA broker -p '22,80,....,' ip