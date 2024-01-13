# Privilege Escalation Step by Step Strategy

1. Check user with id and whoami

2. Have quick look at files in user's home or /var and /opt

3. Run Linux Smart Enumeration, level 0

4. Try SUDO, Cron Jobs, SUID files

5. Run Linux Smart Enumeration, level 1

6. Check for processes running on internal ports, exposing with port forwarding
   
7. Have a look at root processes and versions, searching for exploits

8. Run Linux Smart Enumeration level 2 and/or linPEAS

9. Try Kernel Exploits