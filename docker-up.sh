#!/bin/bash

sudo chmod -R 0777 ./mongodb
docker-compose up -d --remove-orphans
CID=$(docker ps -aqf "name=mongodb")
echo "CID=$CID"
