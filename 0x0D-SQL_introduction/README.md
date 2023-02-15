# 0x0D. SQL - Introduction

# Requirments

### General

* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT
```

### Install MySQL on Ubuntu

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

* Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

# Tasks

#### 0. List databases

* Write a script that lists all databases of your MySQL server.

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```

[solution](0-list_databases.sql)

#### 1. Create a database

* Write a script that creates the database hbtn_0c_0 in your MySQL server.

-> If the database hbtn_0c_0 already exists, your script should not fail
-> You are not allowed to use the SELECT or SHOW statements

```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
```

[solution](1-create_database_if_missing.sql)

#### CREATE DATABASE Statement

```
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] dbname
    [create_option] ...

create_option: [DEFAULT] {
    CHARACTER SET [=] charset_name
  | COLLATE [=] collation_name
  | ENCRYPTION [=] {'Y' | 'N'}
}
```

* An error occurs if the database exists and you did not specify `IF NOT
EXIST`

* `CREATE DATABASE` is not permitted within a session that has an active
`LOCK TABLES` statement.

* A db in MySQL is implemented as a directory containing files that correspond
to tables in the db.Bec. there are no tables in a db when it is initially
created, the CREATE DATABASE statement creates only a dir. under MySQL data
dir.

* When you create a db, let the server manage the dir. and files in it.
Manipulating db dirs can cause inconsistencty.

#### DROP DATABASE Statement

```
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

* DROP DATABASE drops all tables in the database and deletes the database. 
Be very careful with this statement! To use DROP DATABASE, you need the 
DROP privilege on the database. DROP SCHEMA is a synonym for DROP DATABASE.i

* When a database is dropped, privileges granted specifically for the 
database are not automatically dropped. They must be dropped manually.

* IF EXISTS is used to prevent an error from occurring if the database 
does not exist.

* If the default database is dropped, the default database is unset 
(the DATABASE() function returns NULL).
* If you use DROP DATABASE on a symbolically linked database, 
both the link and the original database are deleted.

* DROP DATABASE returns the number of tables that were removed.

* If other files or directories remain in the database directory after 
MySQL removes those just listed, the database directory cannot be removed. 
In this case, you must remove any remaining files or directories manually 
and issue the DROP DATABASE statement again.

#### 3. List tables

Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of mysql command (in the 
following example: mysql is the name of the database)

[solution](3-list_tables.sql)

#### 4. First table

Write a script that created a table called `first_table` in the current
database in your MySQL server.

* `first_table` description:
-> `id` INT     -> `name` VARCHAR(256)
* The db name will be passed as an arg of the `mysql` command.
* If the table `first_table` already exists, your script should
not fail

```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
```

[solution](4-first_table.sql)

##### CREATE TABLE Statement

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [partition_options]
```

*  You must have the CREATE privilege for the table.

#### 5. Full description

Write a script that prints the full description of the table `first_table` 
from the db hbtn_0c_0 in your MySQL server.

* The db name will be passed as an argument of the `mysql` command

[solution](5-full_table.sql)

#### 6. List all in table

Write a script that lists all rows of the table `first_table` from database

* All fields should be printed.

[solution](6-list_values.sql)

#### 7. First add

Write a script that inserts a new row in the table `first_table`.

* New row:
-> id = 89
-> name = Best School

[solution](7-insert_value.sql)

##### INSERT Statement

```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...}
    [AS row_alias[(col_alias [, col_alias] ...)]]
    [ON DUPLICATE KEY UPDATE assignment_list]
```

* `INSERT` inserts new rows into an existing table.

* The `INSERT ... VALUES, INSERT ... VALUES ROW()` and `INSERT ... SET`
forms of the statement insert rows based on explicitily specified values.

* `INSERT ... SELECT` form insert rows selected from another table or tables

* `INSERT ... TABLE` insert rows from a single table.

#### 8. Count 89

Write a script that displays the number of records with id = 89 in 
the table first_table of the database hbtn_0c_0

[solution](8-count_89.sql)

#### 9. Full creation

Write a script that creates a table `second_table` in the db `hbtn_0c_0`
and multiplies rows.

* `second_table` description:
* `id` INT
* `name` VARCHAR(256)
* `score` INT

* If the table `second_table` already exists, your script should not fail.

* Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8

[solution](9-full_creation.sql)

#### 10. List by best

Write a script that lists all records of the table `second_table` and add
multiple rows.

* Results should display both the score and the name (in this order)
* Recoeds should be ordered by score (top first)

[solution](10-top_score.sql)

##### SELECT Statement

```
SELECT
    select_expr [, select_expr] ...
    [into_option]
    [FROM table_references]
    [ORDER BY {col_name}]
        [ASC | DESC]
```

#### 11. Select the best

Write a script that lists all records with a `score >= 10` in the table
`second_table` of the db

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)

[solution](11-best_score.sql)

#### 12. Cheating is bad

Write a script that updates the score of Bob to `10` in the `second_table`

* You are not allowed to use Bob's id value, only the `name` field.

[solution](12-no_cheating.sql)

##### UPDATE Statement

* `UPDATE` is a DML statement that modifies rows in a table.

```
UPDATE table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
```
