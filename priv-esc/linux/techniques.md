# Privilege Escalation Tecniques

## Kernel Exploits
Kernel has the complete control over the OS. After enumerating kernel version with:

```console
$ uname -a
Linux kali 6.3.0-kali1-arm64 #1 SMP Debian 6.3.7-1kali1 (2023-06-29) aarch64 GNU/Linux
```

we can then find exploits with searchsploit or online


## Service Exploits
Services are programs that start with the OS boot and run in background. A service could be vulnerable or could run as root. We can show all processes running as root with:

```console
$ ps aux | grep "^root"

$ PROGRAM -v
```

## Weak File Permissions
We can take advantage from files with too weak permissions. For example:
* `/etc/shadow`: not readable by default (except from root). If readable, we can try to crack the hash. If writable, we can replace the hash with a well-known one
* `/etc/passwd`: historically contained hash (before /etc/shadow). If writable we can enter a known hash after the second semicolumn, it will be used as password. If we can only append in that file, we can insert a new user with the UID=0
* `/`, `/tmp`, `/var/backups`, `/.ssh` or other home folders could inlude insecure backups in which the user may have done backup of important sensitive files

## Sudo 
Sudo lets users run programs with privileges of other users simply adding his password: root by default, other users with -u flag.

Here a list of "legal" ways to escalate privileges:

```console
sudo su
sudo -s
sudo -i
sudo /bin/bash
sudo passwd
```

`sudo -l` instead, can be used to list which programs can be executed with sudo by the current user and may have the possibility to run it with NOPASSWD. This info are contained in `/etc/sudoers`
We can use these programs to perform shell escape sequence or to abuse intended functionality such as read files

### LD_PRELOAD
### LD_LIBRARY_PATH


## Cron Jobs
Cron Jobs are programs the user can schedule to run at specific times/intervals. They run with the security level of the user who owns them. If the Cron Job (or a program called during the schedule) can be modified or replaced (using $PATH), we can perform privilege escalation.

### PATH Env. Variable
If a vulnerable program does not use absolute path, we can modify the environment variable PATH, appending a folder in which we will create our malicious program with the same name.
Using the example below we tell to the system to prefer /tmp folder to the other ones

```console
$ export PATH=/tmp:$PATH
```

### Wildcards
Suppose of a job or weak permission program that executes this line.

```console
$ tar czf /tmp/backup.tar.gz *
```

From GTFobins, we know that we can execute a shell with the following command, so we can create filenames that match complex options
```console
$ tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

$ touch /home/user/--checkpoint=1
$ touch /home/user/--checkpoint-action=exec=shell.elf
```

## SUID / SGID
- string
- strace
- ltrace

## Passwords
Weak password storage end password re-use can be an easy way to escalate privileges.
We can check for:
* History Files, searching for commands run with credentials taken as input
* Config Files, searching for stored password, trying password re-use
* SSH keys, if accessible and stored insecurely we can login with ssh



# NFS
NFS, Network File System, is a distributed file system. Remote users can mount shares and work on it.
Created files imherit the remote user's id and group. To prevent root permissions, NFS has Root Squashing: root permissions are replaced with user nobody and group nogroup.

Using `/etc/exports` we can disable `no_root_squash` option, maintanining root permissions and SUID

```console
# Displays lists to be mount
$ showmount -e TARGET

# Mount a share
mount -o rw,vers=2 TARGET_IP:/tmp LOCAL_FOLDER
```