# Privilege Escalation Step by Step Strategy

1. Check user with `whoami` and groups with `net user {USERNAME}`

2. Have a quick look around for files in User's Desktop/Documents/etc and other common locations (C:\ or C:\Programs Files)
3. Run winPEAS with options `fast`, `searchfast` and `cmd`
 
4. Create a checklist of things for each interesting findings
   
5. Run Seatbelt if nothing found with winPEAS or use [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)

6. Check for internal ports to forward

7. Try Kernel Exploits