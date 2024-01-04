# MongoDB

MongoDB is an open-source NoSQL database management system
`mongo` can be used as CLI tool to interact with the database.

```console
mongo -u {USERNAME} -h {TARGET_IP} -p {PORT}
```

## Commands
| COMMAND | ACTION | DESCRIPTION | 
| :-----: | :----: | :---------: | 
| show dbs | Show Databases | Prints out the databases we can access |
| use {database_name} | Select Database | Set to use the database named {database_name} |
| show collections | Show Collections | Prints out the available collections inside the current database |
| db.{collection_name}.find() | Select Values | Prints out all the data from the table {collection_name} |


## Tips
* Use pretty() after find() to beautify the JSON response