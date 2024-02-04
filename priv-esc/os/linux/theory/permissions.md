# Linux Permissions
Permissions are a relationship between users & groups with files & directories. Below an example:

```console
$ ls -l /bin/file
 -rwxr-xr-x  1  root     root   60416 Gen 12 2024 /bin/file
|----------|   |-----|  |-----|
 permissions    owner    group
```

Permissions are defined for:
- [1st chr] file (`-`) or directory (`d`)
- [1st rwx] Owner/User
- [2nd rwx] Group
- [3rd rwx] Other groups 

### Files
Every file has three sets of permissions
- r [READ]: if set, file content can be read
- w [WRITE]: if set, file content can be changed/modified
- x [EXECUTE]: if set, file can be executed

### Directories
Every file has three sets of permissions
- r [READ]: if set, directory content can be listed
- w [WRITE]: if set, directory content can be changed/modified (create/remove files)
- x [EXECUTE]: if set, directory can't be entered

## SUID and SGID
In addition to rwx, there are other special permissions, represented by `s` character
- `SUID` (or setuid): if set, the file will be executed with owner privileges
- `SGID` (or setgid): if set, the file will be executed with group privileges

The SGID permission can be applied for directories, too: files created within that directory, inherits its group.

```console

-rwsr-xr-x 1 root root 60416 Gen 12 2024 /bin/file
-rwxr-sr-x 1 root root 60416 Gen 12 2024 /bin/file
```


## User and Groups
A user can belong to multiple groups and a group can have multiple users. 
A user primary group has the same name of its user account.

A user is identified by the UID (User Identifier), but there are 3 types of UID:
* Real: the real ID, defined in /etc/passwd
* Effective: normally equals to the real ID, but if a process is executed as another user, it takes that real ID
* Saved: supports the Effective ID temporarily storing the Real ID. Commonly used to ensure SUID processes can switch ID and back.

N.B. The root account is a special account that has the UID=0 and can access every file

