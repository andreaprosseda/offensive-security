# Target Enumeration

The first step, once we gain access to the system is the enumeration. Here the most useful commands we need to know

### Base Commands

`whoami` displays effective user id

```console
whoami
```

`id` provides a general overview of the user's privilege level and group memberships

```console
id
```

`pwd` shows environmental variables

```console
pwd
```

`ls` lists the current directory, with the `-la` parameter shows hidden files, too

```console
ls -la
```

`export PATH` allows to change binary selection based on priority when absolute paths are not used

```console
export PATH=/tmp:$PATH
```

### System Info

`hostname` provides the hostname of the target machine

```console
hostname
```

`uname -a` provides system info, such as kernel used

```console
uname -a
```

`/proc/version` provides information about kernel version and additional data such as compiler installed

```console
cat /proc/version
```

`/etc/issue` provides additional information about OS

```console
cat /etc/issue
```

`/etc/passwd` shows users on the system. Real users are ones with `home` directory

```console
cat /etc/passwd
cat /etc/passwd | grep sh$
cat /etc/passwd | grep home
cat /etc/passwd | cut -d ":" -f 1
```

`env` shows environmental variables

```console
env
```

`history` lists all commands previously typed by the user, could contains usernames and passwords if not correctly handled

```console
history
```

`sudo -l` lists all commands the current user can run with root privileges

```console
sudo -l
```

`SUID` and `SGID` allows files to be executed with the permission level of the file owner or the group owner, respectively

```console
find / -type f -perm -04000 -ls 2>/dev/null
```

`Capabilities`, instead of SUID, help manage privileges at a more granular level
```console
getcap -r / 2>/dev/null
```

## Processes
`ps` lists the running processes

```console
# current shell processes
ps 

# all running processes
ps -A

# running processes with process tree
ps axjf
```

`ps aux` shows processes for all users `a`, dispaying the user that launched the process `u` and showing processes not attached to terminal `x`

```console
ps aux
```

## Network

`ifconfig` lists all network interfaces of the target. Useful for `pivoting`

```console
ifconfig
```

`iproute` to confirm existing network routes

```console
iproute
```

`netstat` provides information on existing connections, uncluding TCP/UDP, PID info, etc

```console
netstat -punta
```

| FLAG | DESCRIPTION | NOTE |
| :------------: | :------------: | ------------ |
| -p | PID | Shows service name and PID |
| -u | UDP | Shows UDP connections |
| -n | Numbers | Doesn't resolve names |
| -t | TCP | Shows TCP connections |
| -a | All | Shows all listening ports and established connections |
| -o | Timers | Shows timers |  
| -i | Interface | Shows interface statistics |
| -l | Listening | Shows listening ports only | 
| -s | Stats | Show network usage statistics by protocol |

`/etc/exports` provides information on NFS (Network File Sharing) configuration

```console
cat /etc/exports
cat /etc/exports | grep no_root_squash
```


## Useful Links
* https://gtfobins.github.io/
