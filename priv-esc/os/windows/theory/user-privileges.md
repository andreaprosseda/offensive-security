# User Privileges

In Windows, user accounts and groups can be assigned specific privileges that grant access to certain abilities.

```console
whoami /priv
```

* SeImpersonatePrivilege: grants the ability to impersonate any access tokens which it can obtain
* SeAssignPrimaryPrivilege: similar to the previous one. It enables a user to assign an access token to a new process
* SeBackupPrivilege: grants read access to all objects to the system
* SeRestorePrivilege: grants write access to all objects on the syatem
* SeTakeOwnershipPrivilege: lets the user take ownership over an object (WRITE_OWNER permission)
* SeDebugPrivilege: used for migrate and getSystem