## Permissions
On NTFS volumes permission can be set to grant or deny access to files and folders

Permissions are:
* Read
* Write
* Modify 
* Read & Execute
* List folder contents
* Full Control

![Alt text](https://assets.tryhackme.com/additional/win-fun1/ntfs-permissions1.png)


## Windows\System32
Windows Operating Systems resides in C:\Windows folder (but it could reside in any drive)

C:\Windows\System32 is one of the most important folder: it holds the important files that are critical for the operating system.


## User Accounts
User accounts can be:
* Administrator: can make changes to the system (add/delete users, modify groups/settings etc)
* Standard User: can only make changes to its folders/files and can't perform system level changes (e.g. install programs)

Users are situated in folder C:\Users.


## User Account Control
The large majority of home users are logged as local administrator.
Since an administrator can make changes to the system, this level is high considering the medium usage and this exposes to risk.
Microsoft introduced User Account Control (UAC): when an administrator user logs into the system, the current session doesn't run with elevated permissions, but when they are required, the OS prompted to confirm the operation.
(it is the blue-yellow shield icon in the right of some programs)
The UAC settings can be changed or even turned off entirely (not recommended).


## System Configuration
System Configuration, or msconfig, helps to diagnose startup issues

## Computer Management