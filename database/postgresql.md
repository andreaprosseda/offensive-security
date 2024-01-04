# PostgreSQL

Postgres is an relational database management system (RDBMS). 
The `psql` CLI tool can be used to interact with the database.

```console
psql -u {USERNAME} -h {TARGET_IP} -p {PORT}
```

## Commands
| COMMAND | ACTION | DESCRIPTION | 
| :-----: | :----: | :---------: | 
| \l | Show Databases | Prints out the databases we can access |
| \dc {database_name} | Select Database | Set to use the database named {database_name} |
| \dt | Show Tables | Prints out the available tables inside the current database |
| SELECT * FROM {table_name} | Select Values | Prints out all the data from the table {table_name} |
