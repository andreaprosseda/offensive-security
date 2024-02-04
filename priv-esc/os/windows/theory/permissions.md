The ultimate goal is to gain a shell running as an Administrator or the System user.

# Users
There are two types of account:
* User Accounts: used to login. Collection of settings and preferences for a unique identity. Local Administrator is created by default
* Service Accounts: used to run services. Cannot be used to sign into Windows. The System account is the default service account with highest privileges of any local account.
  

## Groups
User account can belong to multiple groups, and groups can have multiple users. They allow easier access control to resources.

There are two types of groups:
* Regular groups: have a set list of members. E.g. Administrators, Users, etc
* Pseudo groups: have a dynamic list of members which changes based on certain interactions

## Resources
There are multiple types of resources (objects):
* Files / Directories
* Registry Entries
* Services

If a user or group can perform specific action on a resurce is handled by ACL (Access Control List)

## ACL
Accesso Control List is a controller that gives the possibility to access certain resources, based on permissions. Each ACL has zero or more ACE (Access Control Entries).
Each ACE defines the relationship between a principal and a certain access right.