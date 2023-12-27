# MySQL

MySQL is an relational database management system (RDBMS) that is widely used for managing and organizing data.

```console
mysql -h {TARGET_IP} -u {USERNAME} -p {PASSWORD}
```

# Commands
| COMMAND | DESCRIPTION | 
| :------------: | :------------: | 
| SHOW databases | Prints out the databases we can access |
| USE {database_name} | Set to use the database named {database_name} |
| SHOW tables | Prints out the available tables inside the current database |
| SELECT * FROM {table_name} | Prints out all the data from the table {table_name} |

# Tips
* Check for root authentication
* Check for passwordless authentication