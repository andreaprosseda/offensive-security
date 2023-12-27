# snmpwalk

```console
snmpwalk -c public -v1 -t 10 192.168.1.1 OID
```

# Flags

| OPTIONS | DESCRIPTION | NOTE |
| :------------: | :------------: | ------------ |
| -c | Community String | Sort of password for authentication, default to public |
| -v | Version | Specifies the version of the SNMP |
| -t | Timeout | Sets the timeout for each request |
| OID | Object Identifier | Specific value to walk on the MIB tree |  


Here the values an OID can assume:

| OID | DESCRIPTION |
| :------------: | :------------: |
| 1.3.6.1.2.1.25.1.6.0 | System Processes |
| 1.3.6.1.2.1.25.4.2.1.2 | Running Programs |
| 1.3.6.1.2.1.25.4.2.1.4 | Processes Path |
| 1.3.6.1.2.1.25.2.3.1.4 | Storage Units |
| 1.3.6.1.2.1.25.6.3.1.2 | Software Name |
| 1.3.6.1.4.1.77.1.2.25 | User Accounts |
| 1.3.6.1.2.1.6.13.1.3 | TCP Local Ports |