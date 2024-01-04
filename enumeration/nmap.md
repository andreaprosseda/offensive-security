# Nmap
Nmap, short for Network Mapper, is an open-source tool for network exploration and security auditing. 

```console
nmap {TARGET_IP}

nmap -sT -sU {TARGET_IP}

sudo nmap -Pn -p- -A --min-rate 5000 -oG scan.txt {TARGET_IP}

```

# Additional Flags

| FLAG | DESCRIPTION | NOTE |
| :------------: | :------------: | ------------ |
| -sS | TCP scan [Stealth Mode] | It doesn't complete handshake with ACK. Older firewalls didn't log for uncomplete handshakes, but now is misleading |
| -sT | TCP scan [Connect Mode] | Completes the handshake. It is heavier than -sS because is 3-way |
| -sU | UDP scan | Uses standard methods (empty packets) + Protocol-Specific (like SMTP) |
| -sn | Ping scan | Uses to ping the host, used for Network Sweeping |
| -sV | Service scan | Uses to understand the service that is running on current port |
| -oG | Save Output [Greppable Mode] | Save the output in a file given a filepath | 
| -A | Advanced Information | Detect OS, version, scripts and traceroute |
| -O | OS Fingerprinting | Guess the target's OS inspecting returned packets |


## Nmap Walkthrough

```console
# First Lite scan, default port scanning will scan only the 1000 TCP most popular ports, no UDP
nmap {TARGET_IP}

# Add the ability to identify running services (-sV) and use default scripts (-sC)
sudo nmap -sC -sV {TARGET_IP}

# Scan all ports
sudo nmap -p- --min-rate 5000 -oG scan.txt {TARGET_IP}

# Complete scan on all open ports
sudo nmap -sC -sV -A -oA broker -p '22,80,....,' ip

# Try an UDP scan
sudo nmap -F -sU -sV {TARGET_IP}
```