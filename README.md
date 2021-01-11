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

wget https://downloads.mongodb.com/compass/mongosh_0.6.1_amd64.deb

### Install mongo in the host.

[how-to-install-mongodb-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04)

curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

apt update -y

apt install mongodb-org -y

[init.d](https://mithun.co/tips/init-script-for-mongodb-4-on-wsl-in-ubuntu-18-04/)

curl -o /etc/init.d/mongodb https://raw.githubusercontent.com/mongodb/mongo/master/debian/init.d
chmod +x mongodb

### Change user role

use admin
db.updateUser( "root", { roles : [ "userAdminAnyDatabase","readWriteAnyDatabase" ]} )

(c). Copyright, Ray C Horn, All Rights Reserved.