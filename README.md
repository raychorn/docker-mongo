# mongodb via docker-compose

## Table of Contents

- [Usage](#usage)

## Usage <a name = "usage"></a>

./docker-up.sh

### Install Mongo Client (Ubuntu 20.04)

Using Python to validate the mongodb installation via docker.

./makevenv.sh

### Install mongo db tools

[download/shell](https://www.mongodb.com/try/download/shell)

[download/database-tools](https://www.mongodb.com/try/download/database-tools)

[installation-linux](https://docs.mongodb.com/database-tools/installation/installation-linux/)

### Change user role

use admin
db.updateUser( "root", { roles : [ "userAdminAnyDatabase","readWriteAnyDatabase" ]} )

(c). Copyright, Ray C Horn, All Rights Reserved.