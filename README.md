Django Project
==============

This is a Docker (with docker-compose) environment for Django Project development.

# Installation

1. First, clone this repository:

```bash
$ git clone 
```

2. Init project
```bash
$ make
```

3. Show containers:
```bash
$ make ps
```
This results in the following running containers:

```bash
> $ docker-compose ps
   Name                  Command                 State                          Ports
----------------------------------------------------------------------------------------------------------
adminer       entrypoint.sh docker-php-e ...   Up           0.0.0.0:9000->8080/tcp
core          python manage.py runserver ...   Up           0.0.0.0:8000->8000/tcp0:8025->8025/tcp
postgres      docker-entrypoint.sh postgres    Up           0.0.0.0:5432->5432/tcp
```

4. Run Tests:

```bash
$ make test
```
NOTES:

It is provided to you from the seeder 2 trial users:
1.- Admin role
username: nora
password: norashop
2.- Employee role
username: employee
password: employee

If you would like to see the database, I have a manager installed: adminer.
The port is 0.0.0.0:9000.
The credentials are in the file .env
Remember to select the database engine: PostgreSQL

Custom administrator:
http://localhost:8000/admin

URL Admin Django:
http://localhost:8000/administrator/

Please replace the Slack token in the .env file or you can join my workspace
https://join.slack.com/t/noras-shop/shared_invite/zt-wo5ke73b-pacN_MWqIp7eW9gXl~EBlw
